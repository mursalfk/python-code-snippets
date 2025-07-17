import imaplib
import email
from email.header import decode_header
from email.utils import parsedate_to_datetime
import os
import re
from docx import Document

# Email account credentials
IMAP_SERVER = "<EMAIL_PROVIDER_IMAP_ADDRESS>"
EMAIL_ACCOUNT = "<YOUR_EMAIL>"
PASSWORD = "<YOUR_PASSWORD>"

OUTPUT_DIR = "Fetched_Emails"

def sanitize_filename(name):
    # Remove newlines, tabs, and forbidden characters
    name = re.sub(r'[\r\n\t]', ' ', name)
    name = re.sub(r'[\\/:"*?<>|]+', '', name)
    return name.strip()

def save_email_content(msg, subject, date_str):
    # Create subfolder
    clean_subject = sanitize_filename(subject)[:50]  # limit to 50 chars
    folder_name = f"{clean_subject} [{date_str}]"

    folder_path = os.path.join(OUTPUT_DIR, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Save body as docx
    doc = Document()
    doc.add_heading("Email Body", level=1)

    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            disposition = str(part.get("Content-Disposition"))

            if "attachment" not in disposition and content_type == "text/plain":
                body = part.get_payload(decode=True).decode(errors="ignore")
                doc.add_paragraph(body)
            elif "attachment" in disposition:
                filename = part.get_filename()
                if filename:
                    filename = sanitize_filename(filename)
                    filepath = os.path.join(folder_path, filename)
                    with open(filepath, "wb") as f:
                        f.write(part.get_payload(decode=True))
    else:
        body = msg.get_payload(decode=True).decode(errors="ignore")
        doc.add_paragraph(body)

    doc.save(os.path.join(folder_path, "Body.docx"))

def fetch_emails():
    print("📡 Connecting to mail server...")
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)

    print("🔐 Logging in...")
    mail.login(EMAIL_ACCOUNT, PASSWORD)

    print("📬 Selecting inbox...")
    mail.select("inbox")

    print("🔍 Searching for all emails...")
    status, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()
    print(f"📨 {len(email_ids)} emails found.")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for idx, eid in enumerate(email_ids, 1):
        print(f"📥 Fetching email {idx}/{len(email_ids)}...")
        status, msg_data = mail.fetch(eid, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else "utf-8")
                subject = subject.strip() or "No_Subject"

                # Get date
                date_obj = parsedate_to_datetime(msg["Date"])
                date_str = date_obj.strftime("%Y-%m-%d")

                save_email_content(msg, subject, date_str)

    print("✅ Done fetching & saving all emails.")
    mail.logout()

if __name__ == "__main__":
    print("🚀 Starting email fetch script...\n")
    fetch_emails()
    print("\n🎉 All emails saved in 'Fetched_Emails' folder.")
    print("👋 Goodbye!")
