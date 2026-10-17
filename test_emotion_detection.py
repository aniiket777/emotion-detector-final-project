"""Unit tests for the EmotionDetection package."""
import unittest
from unittest.mock import patch, Mock
import requests
from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test suite for emotion_detector function."""

    def _create_mock_response(self, emotions, status_code=200):
        """Helper to create a mocked requests response."""
        mock_resp = Mock()
        mock_resp.status_code = status_code
        mock_resp.json.return_value = {
            "emotionPredictions": [
                {
                    "emotion": emotions
                }
            ]
        }
        return mock_resp

    @patch("requests.post")
    def test_joy_emotion(self, mock_post):
        """Test detection of joy emotion as dominant."""
        mock_post.return_value = self._create_mock_response({
            "anger": 0.02,
            "disgust": 0.01,
            "fear": 0.01,
            "joy": 0.95,
            "sadness": 0.01
        })
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertAlmostEqual(result["joy"], 0.95)

    @patch("requests.post")
    def test_anger_emotion(self, mock_post):
        """Test detection of anger emotion as dominant."""
        mock_post.return_value = self._create_mock_response({
            "anger": 0.92,
            "disgust": 0.02,
            "fear": 0.01,
            "joy": 0.01,
            "sadness": 0.04
        })
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")
        self.assertAlmostEqual(result["anger"], 0.92)

    @patch("requests.post")
    def test_disgust_emotion(self, mock_post):
        """Test detection of disgust emotion as dominant."""
        mock_post.return_value = self._create_mock_response({
            "anger": 0.03,
            "disgust": 0.91,
            "fear": 0.01,
            "joy": 0.01,
            "sadness": 0.04
        })
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")
        self.assertAlmostEqual(result["disgust"], 0.91)

    @patch("requests.post")
    def test_sadness_emotion(self, mock_post):
        """Test detection of sadness emotion as dominant."""
        mock_post.return_value = self._create_mock_response({
            "anger": 0.02,
            "disgust": 0.02,
            "fear": 0.01,
            "joy": 0.01,
            "sadness": 0.94
        })
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")
        self.assertAlmostEqual(result["sadness"], 0.94)

    @patch("requests.post")
    def test_fear_emotion(self, mock_post):
        """Test detection of fear emotion as dominant."""
        mock_post.return_value = self._create_mock_response({
            "anger": 0.01,
            "disgust": 0.01,
            "fear": 0.93,
            "joy": 0.01,
            "sadness": 0.04
        })
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")
        self.assertAlmostEqual(result["fear"], 0.93)

    def test_blank_input(self):
        """Test that blank and whitespace inputs return None for all emotions."""
        expected = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
        self.assertEqual(emotion_detector(""), expected)
        self.assertEqual(emotion_detector("   "), expected)

    @patch("requests.post")
    def test_http_400_response(self, mock_post):
        """Test that HTTP 400 status returns None for all emotions."""
        mock_resp = Mock()
        mock_resp.status_code = 400
        mock_post.return_value = mock_resp

        result = emotion_detector("some input text")
        expected = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
        self.assertEqual(result, expected)

    @patch("requests.post")
    def test_network_exception(self, mock_post):
        """Test that network exceptions are safely handled returning None for all emotions."""
        mock_post.side_effect = requests.exceptions.ConnectionError("Connection timed out")

        result = emotion_detector("some input text")
        expected = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
