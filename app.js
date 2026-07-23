// Main reservation form handler
const signupForm = document.getElementById("signup-form");
const manufacturerForm = document.getElementById("manufacturer-form");
const distributorForm = document.getElementById("distributor-form");
const investorForm = document.getElementById("investor-form");

function setupFormHandler(formElement, endpoint, formType = "reservation") {
  if (!formElement) return;

  formElement.addEventListener("submit", async (event) => {
    event.preventDefault();

    // Collect form data
    const formData = new FormData(formElement);
    const payload = Object.fromEntries(formData);

    try {
      const response = await fetch(endpoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          ...payload,
          type: formType,
        }),
      });

      const result = await response.json();
      const feedbackElement = formElement.querySelector("#feedback");

      if (result.success) {
        feedbackElement.style.display = "block";
        feedbackElement.className = "feedback success";
        feedbackElement.textContent = result.message || "✓ Thank you! Your submission has been recorded.";
        formElement.reset();
        // Scroll feedback into view
        feedbackElement.scrollIntoView({ behavior: "smooth", block: "nearest" });
      } else {
        feedbackElement.style.display = "block";
        feedbackElement.className = "feedback error";
        feedbackElement.textContent = result.error || "There was an error processing your request.";
      }
    } catch (error) {
      const feedbackElement = formElement.querySelector("#feedback");
      feedbackElement.style.display = "block";
      feedbackElement.className = "feedback error";
      feedbackElement.textContent = "We could not process your request right now. Please try again later.";
    }
  });
}

// Setup main reservation form with real-time validation
function setupReservationForm() {
  if (!signupForm) return;

  const nameInput = document.getElementById("name");
  const emailInput = document.getElementById("email");
  const phoneInput = document.getElementById("phone");
  const countryInput = document.getElementById("country");
  const vehicleInput = document.getElementById("vehicle");
  const usageInput = document.getElementById("usage");
  const timelineInput = document.getElementById("timeline");
  const quantityInput = document.getElementById("quantity");
  const consentInput = document.getElementById("consent");
  const feedback = document.getElementById("feedback");
  const emailHint = document.getElementById("email-hint");
  const phoneHint = document.getElementById("phone-hint");

  let debounceTimer = null;

  function updateHint(id, message, isError) {
    const hint = id === "email" ? emailHint : phoneHint;
    if (hint) {
      hint.textContent = message;
      hint.style.color = isError ? "#ffb8b8" : "#8da4bb";
    }
  }

  function renderFeedback(result) {
    if (!feedback) return;

    if (!result || !result.errors || result.errors.length === 0) {
      feedback.className = "feedback success";
      feedback.textContent = result.reservation_id
        ? `Reservation confirmed. Reference #${result.reservation_id}.`
        : "Looks good. Your reservation request is ready to submit.";
      return;
    }

    feedback.className = "feedback error";
    feedback.textContent = result.errors.join(" \n");
  }

  async function validateInput() {
    const payload = {
      name: nameInput?.value,
      email: emailInput?.value,
      phone: phoneInput?.value,
      country: countryInput?.value,
      vehicle: vehicleInput?.value,
      usage: usageInput?.value,
      timeline: timelineInput?.value,
      quantity: quantityInput?.value,
      consent: consentInput?.checked,
    };

    try {
      const response = await fetch("/validate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      const result = await response.json();

      if (emailHint && emailInput) {
        if (result.errors?.includes("email: invalid email address")) {
          updateHint("email", "Enter a valid email such as name@example.com.", true);
        } else if (emailInput.value.trim()) {
          updateHint("email", "Email format looks good.", false);
        } else {
          updateHint("email", "We'll use this to confirm your reservation.", false);
        }
      }

      if (phoneHint && phoneInput) {
        if (result.errors?.includes("phone: invalid phone number")) {
          updateHint("phone", "Use a phone number with at least 7 digits.", true);
        } else if (phoneInput.value.trim()) {
          updateHint("phone", "Phone number looks good.", false);
        } else {
          updateHint("phone", "Include country code (e.g., +94 for Sri Lanka).", false);
        }
      }

      renderFeedback(result);
    } catch (error) {
      if (feedback) {
        feedback.className = "feedback error";
        feedback.textContent = "Validation service is unavailable right now.";
      }
    }
  }

  function scheduleValidation() {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
      validateInput();
    }, 300);
  }

  // Add event listeners for validation
  const fields = [nameInput, emailInput, phoneInput, countryInput, vehicleInput, usageInput, timelineInput, quantityInput].filter(Boolean);
  fields.forEach((field) => {
    field?.addEventListener("input", scheduleValidation);
    field?.addEventListener("change", scheduleValidation);
  });

  // Setup form submission
  setupFormHandler(signupForm, "/reserve", "reservation");
}

// Setup all forms
setupReservationForm();
setupFormHandler(manufacturerForm, "/submit-inquiry", "manufacturer");
setupFormHandler(distributorForm, "/submit-inquiry", "distributor");
setupFormHandler(investorForm, "/submit-inquiry", "investor");

// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    const href = this.getAttribute("href");
    if (href !== "#" && href.length > 1) {
      e.preventDefault();
      const target = document.querySelector(href);
      if (target) {
        target.scrollIntoView({ behavior: "smooth" });
      }
    }
  });
});

// Add loading state to buttons during submission
document.querySelectorAll("form").forEach((form) => {
  form.addEventListener("submit", function () {
    const button = this.querySelector('button[type="submit"]');
    if (button) {
      button.disabled = true;
      const originalText = button.textContent;
      button.textContent = "Submitting...";

      // Re-enable button after 3 seconds in case of error
      setTimeout(() => {
        button.disabled = false;
        button.textContent = originalText;
      }, 3000);
    }
  });
});
