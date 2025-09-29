import pandas as pd

def find_zombie_sessions(app_events: pd.DataFrame) -> pd.DataFrame:
    df = app_events.copy()

    df["event_timestamp"] = pd.to_datetime(df["event_timestamp"], errors="coerce")

    out = (
        df.groupby("session_id")
          .agg(
              user_id=("user_id", "first"),  # or "max"/pd.Series.mode if needed
              start=("event_timestamp", "min"),
              end=("event_timestamp", "max"),
              scroll_count=("event_type", lambda s: (s == "scroll").sum()),
              click_count=("event_type", lambda s: (s == "click").sum()),
              purchase_count=("event_type", lambda s: (s == "purchase").sum()),
          )
          .reset_index()
    )

    out["session_duration_minutes"] = (out["end"] - out["start"]).dt.total_seconds() / 60

    out = out[
        (out["session_duration_minutes"] >= 30)
        & (out["scroll_count"] >= 5)
        & (out["purchase_count"] == 0)
        & (out["click_count"] / out["scroll_count"] < 0.20)  # safe because scroll_count >= 5
    ]

    out = out.sort_values(by=["scroll_count", "session_id"], ascending=[False, True])
    return out[["session_id", "user_id", "session_duration_minutes", "scroll_count"]]