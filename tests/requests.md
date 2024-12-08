1. llama gen

Request

```bash
curl -X 'POST' \
  'http://0.0.0.0:5000/models/langchain/llama3.2/completion' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"topic": "Tony stark"}'
```
Response

```json
{
  "response": "Tony Stark, also known as Iron Man, is a fictional character created by writer/artist Stan Lee and first appearing in The Incredible Hulk #1 in July 1962. He is the founder and CEO of Stark Industries, a multinational technology corporation that designs and manufactures advanced technologies, including his iconic armor suit. With his genius-level intellect, exceptional physical abilities, and penchant for innovative solutions, Tony Stark has become one of the most recognizable and beloved superheroes in the Marvel Universe."
}
```

2. llama chat

Request

```bash
curl -X 'POST' \
  'http://0.0.0.0:5000/models/langchain/llama3.2/chat' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "input_language": "en",
  "output_language": "fr",
  "input": "Hello World"
}'
```

Response
```json
{
  "response": {
    "lc": 1,
    "type": "constructor",
    "id": [
      "langchain",
      "schema",
      "messages",
      "AIMessage"
    ],
    "kwargs": {
      "content": "Bonjour monde ! (Hello world in French)",
      "response_metadata": {
        "model": "llama3.2:1b",
        "created_at": "2024-12-08T08:00:55.013202183Z",
        "done": true,
        "done_reason": "stop",
        "total_duration": 898453253,
        "load_duration": 16664289,
        "prompt_eval_count": 38,
        "prompt_eval_duration": 235000000,
        "eval_count": 10,
        "eval_duration": 644000000,
        "message": {
          "lc": 1,
          "type": "not_implemented",
          "id": [
            "ollama",
            "_types",
            "Message"
          ],
          "repr": "Message(role='assistant', content='', images=None, tool_calls=None)"
        }
      },
      "type": "ai",
      "id": "run-79d8cfe7-7e33-4e48-b15a-89b38a227bfd-0",
      "usage_metadata": {
        "input_tokens": 38,
        "output_tokens": 10,
        "total_tokens": 48
      },
      "tool_calls": [],
      "invalid_tool_calls": []
    }
  }
}
```

3. Custom Model

Request:

```bash
curl -X 'POST' \
  'http://0.0.0.0:5000/models/custom/example' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"x": 10, "y": 10}'
```

Response:
```json
{
  "response": 20
}
```

4. HF GPT 2 generate
```bash
curl -X 'POST' \
  'http://0.0.0.0:5000/models/gpt2/generate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"text": "Once upon a time",
    "generation_params": {
      "max_length": 200,
      "temperature": 0
    }}'
```

Response:
```json
{
  "response": {
    "generated_text": "Once upon a time\n\nThe sun shines in the sky\n\nAnd the moon shines in the sky\n\nAnd the stars shine in the sky\n\nAnd the stars shine in the sky\n\nAnd the stars shine in the sky\n\nAnd the stars shine in the sky\n\nAnd the stars shine in the sky\n\nAnd the stars shine in the sky\n\nAnd the stars shine in the sky\n\nAnd the stars shine in the sky\n\nAnd the stars shine in the sky\n\nAnd the stars shine in the sky\n\nAnd the stars shine in the sky\n\nAnd the stars shine in the sky\n\nAnd the stars shine in the sky\n\nAnd the stars shine in the sky\n\nAnd the stars shine in the sky\n\nAnd the stars shine in the sky\n\nAnd the stars shine in the sky\n\nAnd the stars shine in the sky\n\nAnd the stars shine in the sky\n\nAnd the",
    "model_info": {
      "model_name": "gpt2",
      "task": "generation"
    }
  }
}
```

5. HF t5 translate

Request
```bash
curl -X 'POST' \
  'http://0.0.0.0:5000/models/t5/translate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"text": "Once upon a time"}'
```

Response:
```json
{
  "response": {
    "generated_text": "Einmal upon upon a time",
    "model_info": {
      "model_name": "t5-small",
      "task": "seq2seq"
    }
  }
}
```