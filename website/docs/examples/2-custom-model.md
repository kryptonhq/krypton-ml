# Custom Model

This guide will walk you through the process of implementing a custom model with Krypton ML. We'll create a simple sentiment analysis model as an example.

## Step 1: Create the Custom Model

First, let's create a simple custom model. Create a new file called `custom_sentiment_model.py` in folder `app`:

```python
from krypton_ml.core.models import KryptonCustomModel
from typing import Dict, Any

class SentimentModel(KryptonCustomModel):
    def __init__(self):
        # Initialize your model here
        # For this example, we're using a very simple rule-based approach
        self.positive_words = set(['good', 'great', 'excellent', 'amazing', 'wonderful'])
        self.negative_words = set(['bad', 'terrible', 'awful', 'horrible', 'poor'])

    def predict(self, input: Dict[str, Any]) -> Dict[str, Any]:
        text = input.get('text', '').lower()
        words = text.split()
        
        positive_count = sum(1 for word in words if word in self.positive_words)
        negative_count = sum(1 for word in words if word in self.negative_words)
        
        if positive_count > negative_count:
            sentiment = 'positive'
        elif negative_count > positive_count:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        
        return {"sentiment": sentiment, "confidence": abs(positive_count - negative_count) / len(words)}
```

## Step 2: Configure Krypton ML

Create a configuration file for Krypton ML. Name it `krypton_config.yaml`:

```yaml
krypton:
  server:
    host: "0.0.0.0"
    port: 8000
  models:
    - name: custom-sentiment-model
      type: custom
      module_path: ./app
      callable: custom_sentiment_model.SentimentModel
      endpoint: sentiment-analysis
      description: "A simple custom sentiment analysis model"
      tags:
        - custom
        - sentiment-analysis
```

Make sure to replace `./app` with the actual folder path to your `custom_sentiment_model.py` file.

## Step 3: Run Krypton ML Server

Now, start the Krypton ML server with your configuration:

```bash
krypton krypton_config.yaml
```

## Step 4: Test the Model

You can now test your custom sentiment analysis model using a simple curl command or any API client:

```bash
curl -X POST http://localhost:8000/sentiment-analysis \
     -H "Content-Type: application/json" \
     -d '{"text": "This product is amazing and wonderful!"}'
```

This should return a JSON response with the sentiment analysis result.

## Conclusion

You've successfully implemented and deployed a custom model using Krypton ML. This example demonstrates how to create a custom model that adheres to the `KryptonCustomModel` interface and how to integrate it into your Krypton ML workflow. You can extend this example by implementing more sophisticated custom models as needed.