# Project 2: Linux File Permissions Security Audit

This project simulates a Linux security audit by identifying files with insecure permissions (777, 666).

## 🔍 Audit Script
The script checks files in the current directory and flags those with overly permissive access.

## 🛠 Tools Used
- Python (os & stat modules)
- Linux terminal
- chmod

## ✅ Skills Demonstrated
- System hardening
- File permission auditing
- Python scripting
- Linux fundamentals

## 🔒 Example Output
⚠️  Insecure: secret1.txt has permissions 0o777  
✅ Secure: safe.txt has permissions 0o600

## 🔐 Project 2: Linux File Permission Audit

This project simulates a file permission audit using Linux commands and Python.
- `audit_permissions.py`: Script to check file permission safety.
- `safe.txt`, `secret1.txt`, `secret2.txt`: Files with different permissions.

