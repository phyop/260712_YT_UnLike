#!/usr/bin/env python3
"""純邏輯單元測試（不需 YouTube API / OAuth）。"""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "cleanup_liked.py"


def load_module():
    spec = importlib.util.spec_from_file_location("cleanup_liked", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"無法載入模組：{MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules["cleanup_liked"] = module
    spec.loader.exec_module(module)
    return module


class SplitKeepUnlikeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.mod = load_module()

    def _videos(self, n: int):
        LikedVideo = self.mod.LikedVideo
        return [
            LikedVideo(
                video_id=f"id{i}",
                title=f"title{i}",
                channel_title=f"ch{i}",
                liked_at=None,
                position=i,
            )
            for i in range(n)
        ]

    def test_keep_nine_from_twelve(self) -> None:
        keep, unlike = self.mod.split_keep_and_unlike(self._videos(12), 9)
        self.assertEqual([v.video_id for v in keep], [f"id{i}" for i in range(9)])
        self.assertEqual([v.video_id for v in unlike], ["id9", "id10", "id11"])

    def test_keep_all_when_fewer_than_keep(self) -> None:
        keep, unlike = self.mod.split_keep_and_unlike(self._videos(3), 9)
        self.assertEqual(len(keep), 3)
        self.assertEqual(unlike, [])

    def test_keep_zero_unlikes_all(self) -> None:
        keep, unlike = self.mod.split_keep_and_unlike(self._videos(5), 0)
        self.assertEqual(keep, [])
        self.assertEqual(len(unlike), 5)

    def test_negative_keep_raises(self) -> None:
        with self.assertRaises(ValueError):
            self.mod.split_keep_and_unlike(self._videos(1), -1)

    def test_generic_forbidden_is_not_quota(self) -> None:
        class Response:
            status = 403

        class Error(Exception):
            resp = Response()
            error_details = [{"reason": "forbidden"}]
            content = b'{"error":{"errors":[{"reason":"forbidden"}]}}'

        self.assertFalse(self.mod.is_quota_or_rate_limit(Error("permission denied")))

    def test_quota_exceeded_stops(self) -> None:
        class Response:
            status = 403

        class Error(Exception):
            resp = Response()
            error_details = [{"reason": "quotaExceeded"}]
            content = b""

        self.assertTrue(self.mod.is_quota_or_rate_limit(Error("quota exhausted")))

    def test_http_429_stops(self) -> None:
        class Response:
            status = 429

        class Error(Exception):
            resp = Response()
            error_details = None
            content = b""

        self.assertTrue(self.mod.is_quota_or_rate_limit(Error("too many requests")))


if __name__ == "__main__":
    unittest.main()
