from flask import Flask, request, jsonify
import urllib.request
import re

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"})

@app.route('/fetch', methods=['GET'])
def fetch_url_content():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400

    try:
        # Opening the URL with a timeout
        with urllib.request.urlopen(url, timeout=10) as resp:
            html_bytes = resp.read()
            # Decode and attempt to convert HTML to plain text
            text = html_bytes.decode('utf-8', errors='ignore')
            # Basic HTML to text conversion using regex
            plain = re.sub(r'<[^>]+>', ' ', text) # Remove HTML tags
            plain = re.sub(r'\s+', ' ', plain).strip() # Normalize whitespace

            # Generate a simple summary: first 200 characters and word count
            summary = plain[:200] + ("..." if len(plain) > 200 else '')
            word_count = len(plain.split())

        return jsonify({
            "url": url,
            "summary": summary,
            "word_count": word_count
        })
    except Exception as e:
        # Return error if fetching or processing fails
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
