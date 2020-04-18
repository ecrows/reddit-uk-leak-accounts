# User Activity from Reddit UK Leak Investigation

On December 6th, 2019, Reddit released a list of 61 accounts that had been banned under suspicion of affiliation with an online influence campaign originating in Russia.

These accounts appeared connected to [a high-profile leak of UK documents on the platform](https://www.reddit.com/r/worldpolitics/comments/dkzlfc/officialsensitive_great_britain_is_practically/).
These accounts reportedly shared commonalities with past accounts they had removed following their investigation into the ["Secondary Infektion"](https://medium.com/dfrlab/top-takes-suspected-russian-intelligence-operation-39212367d2f0) influence campaign, leading Reddit staff to attribute the action to Russia.

From [the official release](https://www.reddit.com/r/redditsecurity/comments/e74nml/suspected_campaign_from_russia_on_reddit/):

> We were recently made aware of a post on Reddit that included leaked documents from the UK. We investigated this account and the accounts connected to it, and today we believe this was part of a campaign that has been reported as originating from Russia.  
>  
> [...]  
>  
>  As a result of this investigation, we are banning 1 subreddit and 61 accounts under our policies against vote manipulation and misuse of the platform. As we have done with previous influence operations, we will also preserve these accounts for a time, so that researchers and the public can scrutinize them to see for themselves how these accounts operated.
>  
> -- /u/worstnerd

This repository provides code to collect the preserved information from the removed Reddit accounts, as well as a json archive of the resulting data.

## The Data

The data collected by this script can be found in `data/author_activity.json`.

The results are stored as a JSON list, according to the following format:

```
[
  {
  "author": "gregoratior",
  "submissions": [...],
  "comments": [...]
  },
  ...
```

The data is not edited, augmented, or filtered in any way.  Usage of this data is subject to the [Reddit API Terms of Use](https://www.reddit.com/wiki/api-terms).

## Requirements

No special software is required for downloading and viewing the JSON data under `/data` (though you may want to avail yourself of `pandas.read_json` if you're using Python).

To re-run the collection code, you will require [psaw](https://github.com/dmarx/psaw) which can be installed by typing:  
```pip install psaw```
