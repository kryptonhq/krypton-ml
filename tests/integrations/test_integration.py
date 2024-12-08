import pytest
import requests
import time

# Configuration
BASE_URL = "http://localhost:5000"
TIMEOUT = 30  # seconds


@pytest.fixture(scope="session", autouse=True)
def wait_for_services():
    """Wait for all services to be ready"""
    max_retries = 30
    retry_interval = 1

    for _ in range(max_retries):
        try:
            # Try to hit any endpoint to check if service is up
            requests.get(f"{BASE_URL}/docs")
            return
        except requests.RequestException:
            time.sleep(retry_interval)

    pytest.fail("Services did not start within the expected timeframe")


class TestLangChainIntegration:
    def test_llama_completion(self):
        """Test LangChain Llama completion endpoint"""
        url = f"{BASE_URL}/models/langchain/llama3.2/completion"
        payload = {"topic": "Tony stark"}

        response = requests.post(url, json=payload, timeout=TIMEOUT)

        assert response.status_code == 200
        data = response.json()
        assert "response" in data
        assert isinstance(data["response"], str)
        assert len(data["response"]) > 0
        assert "Tony" in data["response"]  # Basic content check

    def test_llama_chat_translation(self):
        """Test LangChain Llama chat translation endpoint"""
        url = f"{BASE_URL}/models/langchain/llama3.2/chat"
        payload = {
            "input_language": "en",
            "output_language": "fr",
            "input": "Hello World"
        }

        response = requests.post(url, json=payload, timeout=TIMEOUT)

        assert response.status_code == 200
        data = response.json()
        assert "response" in data
        assert "content" in data["response"]["kwargs"]
        assert "Bonjour" in data["response"]["kwargs"]["content"]


class TestCustomModelIntegration:
    def test_custom_model_addition(self):
        """Test custom model addition endpoint"""
        url = f"{BASE_URL}/models/custom/example"
        payload = {"x": 10, "y": 10}

        response = requests.post(url, json=payload, timeout=TIMEOUT)

        assert response.status_code == 200
        data = response.json()
        assert "response" in data
        assert data["response"] == 20


class TestHuggingFaceIntegration:
    def test_gpt2_generation(self):
        """Test GPT-2 text generation endpoint"""
        url = f"{BASE_URL}/models/gpt2/generate"
        payload = {
            "text": "Once upon a time",
            "generation_params": {
                "max_length": 200,
                "temperature": 0
            }
        }

        response = requests.post(url, json=payload, timeout=TIMEOUT)

        assert response.status_code == 200
        data = response.json()
        assert "response" in data
        assert "generated_text" in data["response"]
        assert data["response"]["generated_text"].startswith("Once upon a time")
        assert len(data["response"]["generated_text"]) > len(payload["text"])

        # Check model info
        assert "model_info" in data["response"]
        assert data["response"]["model_info"]["model_name"] == "gpt2"
        assert data["response"]["model_info"]["task"] == "generation"

    def test_t5_translation(self):
        """Test T5 translation endpoint"""
        url = f"{BASE_URL}/models/t5/translate"
        payload = {"text": "Once upon a time"}

        response = requests.post(url, json=payload, timeout=TIMEOUT)

        assert response.status_code == 200
        data = response.json()
        assert "response" in data
        assert "generated_text" in data["response"]
        assert len(data["response"]["generated_text"]) > 0

        # Check model info
        assert "model_info" in data["response"]
        assert data["response"]["model_info"]["model_name"] == "t5-small"
        assert data["response"]["model_info"]["task"] == "seq2seq"


def test_invalid_endpoint():
    """Test behavior with invalid endpoint"""
    url = f"{BASE_URL}/models/nonexistent"
    response = requests.post(url, json={})
    assert response.status_code == 404


@pytest.mark.parametrize("endpoint,payload", [
    ("/models/gpt2/generate", {}),  # Missing text
    ("/models/custom/example", {"x": 10}),  # Missing y
    ("/models/langchain/llama3.2/completion", {}),  # Missing topic
])
def test_invalid_payloads(endpoint, payload):
    """Test behavior with invalid payloads"""
    url = f"{BASE_URL}{endpoint}"
    response = requests.post(url, json=payload, timeout=TIMEOUT)
    assert response.status_code in [400, 422]  # Either bad request or validation error