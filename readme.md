Tihs MCP Server will help MCP Clients to talk to Scanner API, where below API can be called with SHA256 of a file

''' Sample Request

curl -X POST http://localhost:8000/scan/hash \
  -H "Content-Type: application/json" \
  -d '{"hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"}'



''' Sample Response

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