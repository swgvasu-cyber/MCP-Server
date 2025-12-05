MCP Server – Scanner API Bridge

This MCP Server enables MCP Clients to interact with a backend Scanner API using a simple, unified interface.
Clients can submit a SHA-256 hash of a file and receive malware reputation details aggregated from multiple vendors.

🚀 Features

Accepts SHA-256 file hashes

Communicates with backend Scanner APIs (e.g., VirusTotal-style)

Returns:

Malicious vendor count

Suspicious vendor count

Full raw scanner JSON

🔗 Endpoint Overview
POST /scan/hash

Submit a SHA-256 hash to retrieve malware scan results.

📤 Sample Request
curl -X POST http://localhost:8000/scan/hash \
  -H "Content-Type: application/json" \
  -d '{"hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"}'

📥 Sample Response
{
  "malicious_vendors": 42,
  "suspicious_vendors": 3,
  "raw_json": {
    "data": {
      "type": "file",
      "id": "d41d8cd98f00b204e9800998ecf8427e",
      "attributes": {
        "last_analysis_stats": {
          "malicious": 42,
          "suspicious": 3,
          "undetected": 35,
          "timeout": 1
        },
        "last_analysis_results": {
          "Avast": {
            "category": "malicious",
            "engine_name": "Avast",
            "result": "Win32:Malware-gen"
          },
          "Kaspersky": {
            "category": "malicious",
            "engine_name": "Kaspersky",
            "result": "Trojan.Win32.Inject.gen"
          }
        }
      }
    }
  }
}

📦 Project Structure (Example)
mcp-server/
├── server.py
├── manifest.json
├── README.md
└── requirements.txt

▶️ Running the MCP Server
python server.py


Server defaults to:

http://localhost:8000

🧩 Integrating with an MCP Client

Your MCP Client can connect to this server and call the scan/hash endpoint by simply sending:

{ "hash": "<SHA256_VALUE>" }


The MCP Server handles forwarding, parsing, and returning normalized results.