# YouTube Tracking Specification

## Purpose

Maintain a historical record of channel performance so strategy is based on trend data rather than memory.

## Channel identity

- Channel: Laxman Nepal
- Channel ID: `UCFl4DYgZNA-XuFTTihh-l9w`
- Country: Nepal
- Default language: Nepali

## Snapshot baseline — 25 Aug 2026

- Subscribers: 657
- Lifetime views: 45,696
- Videos: 155
- 30-day subscriber gain: 28
- 30-day view gain: 3,986
- 30-day uploads: 4

## Daily/periodic fields

### Channel-level

- Date
- Subscribers
- Total views
- Video count
- Subscriber delta
- View delta
- Upload delta

### Video-level

- Video ID
- Title
- Publish date
- Format
- Topic pillar
- Views
- Likes
- Comments
- Subscribers gained
- Watch time
- Average view duration
- Retention
- Impressions
- CTR
- Traffic source
- Geography

## Derived metrics

### Subscriber conversion

`subscribers gained / views × 100`

### View velocity

`views gained / hours since publication`

### Content efficiency

`useful audience outcome / production effort`

The exact formula can evolve after sufficient data exists.

## Dashboard questions

Every weekly report should answer:

1. Is growth accelerating or slowing?
2. Which topics create subscribers?
3. Which topics create views but little loyalty?
4. Which videos have strong packaging but weak retention?
5. Which videos have strong retention but weak packaging?
6. What should be repeated?
7. What should be stopped?
8. What should be tested?

## Alert rules

Potential alerts:

- Subscriber growth below rolling baseline
- Major view decline
- Strong video breakout
- Topic cluster breakout
- Upload consistency failure
- Unusual traffic pattern

## Data integrity

Do not overwrite historical snapshots. Append new snapshots so growth can be reconstructed.

## Important limitation

API availability and metric granularity vary by connected service. Where an exact Studio metric is unavailable, mark it as unavailable rather than estimating it silently.
