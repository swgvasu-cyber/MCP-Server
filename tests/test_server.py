import pytest
import json
from unittest.mock import AsyncMock, patch
import sys
sys.path.insert(0, 'mcp_server')

from test import scan_hash, post_json

@pytest.mark.asyncio
async def test_scan_hash_success():
    mock_response = {
        "malicious_vendors": 0,
        "suspicious_vendors": 0,
        "raw_json": {"data": {"id": "test123"}}
    }
    
    with patch('test.post_json', new_callable=AsyncMock) as mock_post:
        mock_post.return_value = mock_response
        result = await scan_hash("e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
        
        assert json.loads(result) == mock_response
        mock_post.assert_called_once_with("/scan/hash", {"hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"})

@pytest.mark.asyncio
async def test_scan_hash_backend_error():
    with patch('test.post_json', new_callable=AsyncMock) as mock_post:
        mock_post.return_value = {"error": "Backend returned 500"}
        result = await scan_hash("abc123")
        
        assert "error" in json.loads(result)
