# tracklist_to_timeindex
Converts a music track list with track lengths to a YouTube-compatible time index.

The timestamps can be anywhere on the line. Lines without timestamps are not affected in any way. HH:MM:SS format is supported in both input and output.

Depending on the accuracy of track lengths, the time indexes might accumulate error towards the end of the list. Always verify the end result by hand if this is bothers you.

## Usage

Make a nice track list with track lengths:
```
$ cat example.txt
3:45 The Body of Sensations
4:51 Red Anthem
4:27 Surprise (BUCHIAGE TRANCE Remix)
4:23 Gemini (2013 Remaster)
4:26 Cette Pendule
5:04 Unknownbreak (2013 Remaster)
4:51 Global Spinning
5:00 Flashbat (2013 Remaster)
4:01 The Body of Sensations -separate-
6:16 Red Anthem -separate-
6:09 Surprise (BUCHIAGE TRANCE Separate Remix)
5:35 Cette Pendule -separate-
6:18 Global Spinning -separate-
```

Turn it into time index list:
```
$ ./timeindex.py <example.txt
0:00 The Body of Sensations
3:45 Red Anthem
8:36 Surprise (BUCHIAGE TRANCE Remix)
13:03 Gemini (2013 Remaster)
17:26 Cette Pendule
21:52 Unknownbreak (2013 Remaster)
26:56 Global Spinning
31:47 Flashbat (2013 Remaster)
36:47 The Body of Sensations -separate-
40:48 Red Anthem -separate-
47:04 Surprise (BUCHIAGE TRANCE Separate Remix)
53:13 Cette Pendule -separate-
58:48 Global Spinning -separate-
```
