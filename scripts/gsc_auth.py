from google_auth_oauthlib.flow import InstalledAppFlow

flow = InstalledAppFlow.from_client_secrets_file(
    r"D:\limhansin\vision2025\reporthub\scripts\client_secret.json",
    scopes=["https://www.googleapis.com/auth/webmasters"]
)

try:
    creds = flow.run_local_server(port=0)
except:
    creds = flow.run_console()

with open(r"D:\limhansin\vision2025\reporthub\scripts\token.json", "w") as token:
    token.write(creds.to_json())

print("[OK] token.json 생성 완료")

