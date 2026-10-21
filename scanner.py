import urllib.request
import urllib.error
from urllib.parse import urlparse
from datetime import datetime

SECURITY_HEADERS = {
    "Content-Security-Policy": "Helps prevent content injection attacks.",
    "Strict-Transport-Security": "Enforces HTTPS connections.",
    "X-Content-Type-Options": "Helps prevent MIME-type sniffing.",
    "X-Frame-Options": "Helps protect against clickjacking.",
    "Referrer-Policy": "Controls referrer information.",
    "Permissions-Policy": "Controls access to browser features.",
}


def scan_website(url):
    url = url.strip()

    if not url.startswith(("https://", "http://")):
        url = "https://" + url

    parsed_url = urlparse(url)

    if parsed_url.scheme not in ("https", "http") or not parsed_url.hostname:
        print("Error: Please enter a valid HTTP or HTTPS website URL.")
        return

    results = []

    def report(message=""):
        print(message)
        results.append(message)

    report("=" * 55)
    report("                 WebShield Scanner")
    report("=" * 55)
    report(f"Target: {url}")
    report(f"Scan date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report("\nChecking HTTP security headers...\n")

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "WebShield/1.0",
            "Origin": "https://webshield-test.example",
        },
        method="GET",
    )

    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            headers = response.headers
            status = response.status
            final_url = response.geturl()

        report(f"HTTP Status: {status}")
        report(f"Final URL: {final_url}")
        report(
            f"HTTPS: {'Enabled' if urlparse(final_url).scheme == 'https' else 'Not enabled'}"
        )

        passed = 0
        missing = 0

        for header, description in SECURITY_HEADERS.items():
            value = headers.get(header)

            if value:
                report(f"\n[FOUND] {header}: {value}")
                report(f"        {description}")
                passed += 1
            else:
                report(f"\n[MISSING] {header}")
                report(f"          {description}")
                missing += 1

        report("\nChecking CORS configuration...\n")
        cors_origin = headers.get("Access-Control-Allow-Origin")

        if cors_origin == "*":
            report("[WARNING] CORS allows all origins (*).")
            report("Review whether public access is intentional.")
        elif cors_origin:
            report(f"[FOUND] Access-Control-Allow-Origin: {cors_origin}")
            report("Compare this value with your intended allowed origins.")
        else:
            report("[INFO] No Access-Control-Allow-Origin header found.")
            report("This response does not show CORS permission for this test origin.")

        report("\n" + "=" * 55)
        report("                 Scan Summary")
        report("=" * 55)
        report(f"Security headers found: {passed}")
        report(f"Security headers missing: {missing}")
        report("\nNote: Missing headers do not automatically mean")
        report("the website is vulnerable. Review results in context.")

    except urllib.error.HTTPError as error:
        report(f"HTTP Error: {error.code} {error.reason}")
    except urllib.error.URLError as error:
        report(f"Connection Error: {error.reason}")
    except TimeoutError:
        report("Error: The request timed out.")
    except ValueError as error:
        report(f"Invalid URL: {error}")
    except Exception as error:
        report(f"Unexpected error: {error}")

    try:
        with open("scan_report.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(results) + "\n")
        print("\nReport saved to scan_report.txt")
    except OSError as error:
        print(f"\nCould not save report: {error}")


if __name__ == "__main__":
    target = input("Enter a website URL you are authorized to scan: ")
    scan_website(target)