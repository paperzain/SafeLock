# SafeLock 🔐
SafeLock is a password detective, analyzing every character to uncover weak patterns, common phrases, and vulnerabilities. It rates password strength, checks against compromised databases, and provides actionable tips to create strong, secure, and unguessable passwords, keeping your digital secrets safe.
<p align="left">
<img width="1536" height="1024" alt="SafeLock Workflow Diagram" src="https://github.com/user-attachments/assets/33b1e99d-ce71-4b20-b279-0d8d16a0315c" />

</p>

## Key Components:

1. **User Access Layer**
   Users authenticate via secure credentials or multi-factor authentication (MFA). Only authorized users can access the system.

2. **Encryption Module**  
   Sensitive data is encrypted both at rest and in transit, ensuring that even if intercepted, the data remains unreadable.

3. **Access Control Engine**  
   Permissions are enforced based on user roles, defining who can read, write, or modify resources.

4. **Audit & Logging Layer**  
   All actions and access events are tracked to provide full visibility for compliance and forensic purposes.

5. **Secure Storage / Vault**  
   Encrypted storage houses critical data and secrets, fully protected by encryption and access controls.

### Data Flow

Users interact with the system through the access layer → requests are validated by the access control engine → data is encrypted/decrypted as needed → actions are logged → sensitive data is securely stored in the vault.

This layered approach makes SafeLock a robust solution for protecting sensitive information while maintaining accountability and compliance. 

## ✨ Features

- Real-time password strength analysis  
- Common password detection  
- Time-to-crack prediction  
- Show/Hide password with a tiny cute eye icon    

---

## 🛠 Tech

- **Backend:** Python (Flask)  
- **Frontend:** HTML, CSS, JavaScript  
- **Hosting:** Vercel (Serverless Python)  

https://github.com/paperzain/SafeLock/blob/main/SafeLock%20Workflow%20Diagram.png
