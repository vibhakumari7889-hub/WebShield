# WebShield – Automated Web Security Scanner

## Project Overview

WebShield is a beginner-friendly cybersecurity project developed using Python. It checks HTTP security headers, HTTPS usage, and the presence of CORS response headers for a specified website.

The scanner displays its findings in the terminal and saves the scan results to a text report.

## Objectives

- Check whether a website responds successfully.
- Identify common HTTP security headers.
- Check whether the final URL uses HTTPS.
- Inspect the `Access-Control-Allow-Origin` response header.
- Save scan results in a report file for review.

## Features

- Checks six common HTTP security headers.
- Displays the HTTP response status.
- Reports whether the final URL uses HTTPS.
- Inspects the CORS response header.
- Handles common connection and HTTP errors.
- Saves results to `scan_report.txt`.

## Technologies Used

- Python 3
- Python standard library: `urllib`, `datetime`
- IBM Bob IDE

No additional Python packages are required.

## Security Headers Checked

1. `Content-Security-Policy`
2. `Strict-Transport-Security`
3. `X-Content-Type-Options`
4. `X-Frame-Options`
5. `Referrer-Policy`
6. `Permissions-Policy`

## Project Structure

```text
WebShield/
├── scanner.py
├── scan_report.txt
└── README.md
```

`scan_report.txt` is generated when the scanner runs.

## Requirements

- Python 3 installed on your computer.
- Internet connection.
- Permission to scan the target website.

## How to Run

1. Open the project folder in IBM Bob or a terminal.
2. Open the terminal in the project directory.
3. Run the command:

   `python scanner.py`

4. Enter a website URL when prompted, for example:

   `https://example.com`

5. Review the scan results in the terminal.
6. Open `scan_report.txt` to review the saved results.

## Testing

The scanner was tested with `https://example.com`.

The test returned HTTP status `200` and confirmed that the final URL used HTTPS. The scanner also checked the six security headers and the CORS response header, then saved the output to `scan_report.txt`.

Results may vary depending on the website and its configuration.

## Limitations

- The scanner checks response headers; it does not perform a complete security audit.
- A missing header does not automatically mean a website is vulnerable.
- CORS assessment requires understanding the website's intended access policy.
- The scanner uses a basic HTTP GET request and does not test every endpoint or HTTP method.
- Network errors or server restrictions may affect results.

## Responsible Use

Use WebShield only on websites you own or have permission to assess. This tool is intended for educational purposes and basic security-header inspection. It does not guarantee that a website is secure.

## Future Improvements

- Export reports to additional formats.
- Add automated tests.
- Improve URL validation and reporting.
- Provide clearer recommendations for each finding.

## Author

Developed as a cybersecurity learning project for the IBM SkillBuild National Cybersecurity Bootcamp.
