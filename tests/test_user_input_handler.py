import unittest

from aegis_core import process_user_input


class ProcessUserInputTests(unittest.TestCase):
    def test_accepts_valid_email_and_password(self):
        result = process_user_input({
            "email": "user@example.com",
            "password": "SecurePass123!"
        })

        self.assertTrue(result["success"])
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["validated_data"]["email"], "user@example.com")

    def test_rejects_invalid_email_and_short_password(self):
        result = process_user_input({
            "email": "not-an-email",
            "password": "short"
        })

        self.assertFalse(result["success"])
        self.assertIn("email", result["errors"][0])
        self.assertIn("password", result["errors"][1])


if __name__ == "__main__":
    unittest.main()
