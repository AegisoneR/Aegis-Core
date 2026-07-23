// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title AegisOne Token (AEGIS)
 * @dev BEP-20 Token for Aegis One Electric Mobility Platform
 * Contract deployed on Binance Smart Chain (BSC)
 */

interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

contract AegisOneToken is IERC20 {
    string public constant name = "Aegis One";
    string public constant symbol = "AEGIS";
    uint8 public constant decimals = 18;
    uint256 private _totalSupply = 1000000000 * 10 ** uint256(decimals); // 1 billion tokens
    
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;
    
    address public owner;
    bool private _paused = false;
    
    event PauseToggled(bool paused);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    modifier whenNotPaused() {
        require(!_paused, "Token transfers are paused");
        _;
    }
    
    constructor() {
        owner = msg.sender;
        _balances[msg.sender] = _totalSupply;
        emit Transfer(address(0), msg.sender, _totalSupply);
    }
    
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }
    
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }
    
    function transfer(address recipient, uint256 amount) public override whenNotPaused returns (bool) {
        require(recipient != address(0), "Cannot transfer to zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");
        
        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }
    
    function approve(address spender, uint256 amount) public override returns (bool) {
        require(spender != address(0), "Cannot approve zero address");
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }
    
    function allowance(address owner_addr, address spender) public view override returns (uint256) {
        return _allowances[owner_addr][spender];
    }
    
    function transferFrom(address sender, address recipient, uint256 amount) public override whenNotPaused returns (bool) {
        require(sender != address(0), "Cannot transfer from zero address");
        require(recipient != address(0), "Cannot transfer to zero address");
        require(_balances[sender] >= amount, "Insufficient balance");
        require(_allowances[sender][msg.sender] >= amount, "Allowance exceeded");
        
        _balances[sender] -= amount;
        _balances[recipient] += amount;
        _allowances[sender][msg.sender] -= amount;
        
        emit Transfer(sender, recipient, amount);
        return true;
    }
    
    // Owner functions
    function transferOwnership(address newOwner) public onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
    
    function togglePause() public onlyOwner {
        _paused = !_paused;
        emit PauseToggled(_paused);
    }
    
    function burn(uint256 amount) public onlyOwner {
        require(_balances[msg.sender] >= amount, "Insufficient balance to burn");
        _balances[msg.sender] -= amount;
        _totalSupply -= amount;
        emit Transfer(msg.sender, address(0), amount);
    }
    
    function mint(address to, uint256 amount) public onlyOwner {
        require(to != address(0), "Cannot mint to zero address");
        _balances[to] += amount;
        _totalSupply += amount;
        emit Transfer(address(0), to, amount);
    }
}
