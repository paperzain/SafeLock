"""
=========================================================
                  SafeLock - Password Checker
=========================================================

SafeLock is a lightweight password strength checker built with Flask.
It evaluates passwords in real-time and provides:
  - Strength scoring (Very Weak to Very Strong)
  - Crack time estimation
  - Detection of common passwords and patterns
  - Actionable tips to improve password security
  - Rate limiting to prevent abuse

Author: Syed Ali Zain Ul Abidin
Version: 1.0

Usage:
  1. Run this script using Python 3.x
  2. Access the web interface at http://localhost:5000/
  3. Enter passwords to get real-time strength feedback

Notes:
  - Requires 'common_passwords.txt' from SecLists for common password checking.
  - Uses Flask session security settings for better safety.
=========================================================
"""

from flask import Flask, render_template, request, jsonify
import re
import time
from collections import defaultdict
import html
import math
import os

# ----------------- Flask App Configuration -----------------
app = Flask(__name__)

# Session security settings for SafeLock
app.config['SESSION_COOKIE_SAMESITE'] = 'Strict'     # Protect against CSRF
app.config['SESSION_COOKIE_SECURE'] = True           # Send cookies only over HTTPS
app.config['SESSION_COOKIE_HTTPONLY'] = True         # Prevent JavaScript access
app.config['SESSION_COOKIE_NAME'] = '__Secure-Session'
app.secret_key = os.environ.get('FLASK_SECRET', 'xxxxxxx')  # Secret key for sessions

# ----------------- Rate Limiting Store -----------------
# Keeps track of request timestamps per IP to prevent abuse
rate_limit_store = defaultdict(list)
