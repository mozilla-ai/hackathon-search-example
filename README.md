# hackathon-search-example
Minimal python code showing a barebones AI search assistant tool running with llamafile, exa MCP, and any-agent.

To run:

```
uv sync
source .venv/bin/activate
python search_agent.py
```

The default prompt sent to the agent is:

```
What are 5 tv shows that are trending in September 2026? Please provide the name of the show, the platform, the exact release date, the genre,
the rating (better using a uniform metric, eg. tomatometer), and a brief description of each. Conclude with a References section with a list
of URLs you have used to prepare your answer.
```

# Expected output
Note that the output can change significantly depending on the model family and size you choose. With a Qwen3.5:9B model we got the following answer.

Based on my research, here are 5 TV shows trending in September 2026:

## 1. The Gentlemen: Season 2
- **Platform:** Netflix
- **Release Date:** September 3, 2026
- **Genre:** Action Comedy / Crime Drama
- **Rating:** 75% (Tomatometer)
- **Description:** Guy Ritchie's crime-comedy series returns with Eddie Horniman (Theo James) expanding his criminal empire overseas. The season moves to Italy where Eddie and Susie Glass (Kaya Scodelario) confront the Italian mafia. Signature style, sharp dialogue, and lethal consequences await.

## 2. Monster: The Lizzie Borden Story
- **Platform:** Netflix
- **Release Date:** September 17, 2026
- **Genre:** Crime Drama / True Crime / Psychological Horror
- **Rating:** N/A (Previous seasons averaged 42-57% on Tomatometer)
- **Description:** Ryan Murphy and Ian Brennan's anthology series returns with its fourth installment, focusing on the infamous 1892 axe murders. Starring Ella Beatty as Lizzie, the series explores the first female "monster" in the anthology, featuring Charlie Hunnam, Rebecca Hall, and Sarah Paulson.

## 3. Brothers
- **Platform:** Apple TV+
- **Release Date:** September 23, 2026
- **Genre:** Comedy
- **Rating:** N/A (New series)
- **Description:** A meta-comedy starring Matthew McConaughey and Woody Harrelson as fictionalized versions of themselves. Their lifelong friendship spirals when they uncover a secret they might actually be biological brothers. Explores friendship, family, fame, and the line between myth and reality.

## 4. Chad Powers: Season 2
- **Platform:** Hulu
- **Release Date:** September 3, 2026
- **Genre:** Sports Comedy
- **Rating:** 59% (Tomatometer - Season 1)
- **Description:** Glen Powell returns as Russ Holliday/Chad Powers, a disgraced quarterback maintaining his disguise as a walk-on player. All six episodes release simultaneously as Chad faces increasing suspicion while trying to lead his team to the College Football Playoff.

## 5. Plastic Beauty
- **Platform:** Netflix
- **Release Date:** September 17, 2026
- **Genre:** Psychological Drama / Medical Drama / Suspense
- **Rating:** N/A (New series)
- **Description:** A Japanese Netflix Original set against Japan's cosmetic surgery industry. Fumi Numata (Mayu Matsuoka), a gifted surgeon, clashes with celebrity cosmetic surgeon Rin Tohyama (Riisa Naka) over opposing philosophies about beauty and healing. Explores whether the pursuit of beauty is hope or a curse.

---

## References
1. https://www.rottentomatoes.com/browse/tv_series_browse
2. https://www.hollywoodreporter.com/lists/2026-tv-premiere-dates-calendar/
3. https://www.forbes.com/sites/erikkain/2026/08/29/everything-coming-to-netflix-september-2026/
4. https://www.tvline.com/2236241/netflix-fall-2026-schedule-movies-tv-shows/
5. https://www.apple.com/tv-pr/news/2026/06/apple-tvs-new-comedy-series-brothers-starring-matthew-mcconaughey-and-woody-harrelson-to-make-global-debut-on-wednesday-september-23/
6. https://deadline.com/lists/most-anticipated-tv-shows-2026/
7. https://www.nbcuniversal.com/article/nbc-sets-fall-premiere-dates-2026-27-season
8. https://www.whats-on-netflix.com/news/the-final-problem-netflix-release-date/
9. https://about.netflix.com/en/news/plasticbeauty-maintrailer-and-keyart
10. https://variety.com/2026/tv/news/the-gentlemen-season-2-release-date-netflix-1236805700/
11. https://deadline.com/2026/07/chad-powers-season-2-premiere-date-hulu-1237018234/
12. https://www.netflix.com/tudum/articles/monster-season-4-lizzie-borden-release-date-cast-news
13. https://en.wikipedia.org/wiki/The_Gentlemen_(2024_TV_series)
14. https://en.wikipedia.org/wiki/Brothers_(2026_TV_series)
15. https://www.tvguide.com/news/ultimate-guide-what-to-watch-netflix-hulu-prime-video-hbo-max-september-2026/

---

**Important Note:** This information is based on scheduled release dates and promotional materials from search results dated September 2026. As an AI, I cannot predict actual future events. The data represents planned content rather than actual trending shows, as September 2026 is a future date. Actual ratings, viewer reception, and show availability may differ from this information.