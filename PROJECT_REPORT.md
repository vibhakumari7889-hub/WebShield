# WebShield – Project Report

## 1. Project Title

**WebShield: Automated Web Security Scanner**

## 2. Introduction

WebShield is a Python-based cybersecurity learning project that checks common HTTP security headers, HTTPS usage, and the presence of a CORS response header.

The project demonstrates how a simple automated tool can collect basic website response information and present it in a readable report.

## 3. Problem Statement

Website security configurations can be difficult for beginners to inspect manually. WebShield provides a simple way to check selected HTTP response headers and identify areas that may need further review.

## 4. Project Objectives

- Inspect HTTP response status codes.
- Check whether the final website URL uses HTTPS.
- Identify the presence or absence of six common HTTP security headers.
- Inspect the `Access-Control-Allow-Origin` response header.
- Display results in the terminal.
- Save scan results to a text file.

## 5. Tools and Technologies

- **Programming language:** Python 3
- **Development environment:** IBM Bob IDE
- **Python modules:** `urllib`, `datetime`
- **Operating environment:** Windows

The project uses Python's standard library and does not require additional packages.

## 6. Methodology

The scanner follows these steps:

1. Accepts a website URL from the user.
2. Adds HTTPS when the URL does not include an HTTP scheme.
3. Validates the basic URL structure.
4. Sends an HTTP GET request to the target website.
5. Reads the response status, final URL, and HTTP headers.
6. Checks six selected security headers.
7. Inspects the CORS response header.
8. Displays findings in the terminal.
9. Saves the results in `scan_report.txt`.

## 7. Security Headers Checked

The project checks the following headers:

- **Content-Security-Policy:** Helps restrict permitted content sources.
- **Strict-Transport-Security:** Instructs browsers to use HTTPS for future connections.
- **X-Content-Type-Options:** Helps prevent MIME-type sniffing.
- **X-Frame-Options:** Provides protection against certain framing and clickjacking scenarios.
- **Referrer-Policy:** Controls referrer information sent by browsers.
- **Permissions-Policy:** Controls access to selected browser features.

## 8. Testing and Results

The scanner was executed against `https://example.com` as an initial connectivity test.

Observed results:

| Test | Result |
|---|---|
| HTTP response status | 200 |
| Final URL uses HTTPS | Yes |
| Security headers found | 0 |
| Security headers missing | 6 |
| CORS response header | Not found |
| Text report saved | Yes |

The results reflect the response received during the test. Missing headers do not automatically establish that a website is vulnerable. A proper assessment requires reviewing the site's requirements and security configuration.

## 9. Output

The scanner displays the scan results in the terminal and saves them in:

`scan_report.txt`

The report includes the target URL, scan time, HTTP response details, security-header findings, CORS observation, and a summary.

## 10. Limitations

- The project performs basic response-header inspection, not a complete penetration test.
- It does not assess every endpoint, HTTP method, or