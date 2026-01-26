from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        # النص الذي سنعالجه
        input_text = "cloud computing is powerful"
        # عملية المعالجة المطلوبة في النشاط
        processed_text = input_text.upper()
        
        response = f"Original: {input_text}\nProcessed Result: {processed_text}"
        self.wfile.write(response.encode())
        return
