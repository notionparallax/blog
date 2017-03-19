---
layout: post
title: OpenAsset REST API confusion
date: 2014-07-04 05:04:08.000000000 +10:00
type: post
published: true
status: publish
categories: []
tags:
- confusion
- internet
- OpenAsset
- programming
- REST
description:
meta:
  _publicize_facebook_user: https://www.facebook.com/ben.doherty1
  _publicize_twitter_user: "@notionparallax"


  _wpas_mess: Does anyone understand the OpenAsset REST API?


  dsq_thread_id: '4503553490'

---

The <a href="http://axomic.com/">Axomic</a> <a href="https://www.axomic.com/media">OpenAsset</a> <a title="The REST docs" href="http://help.axomic.com/07_Technical_Stuff/APIs_and_Integration/REST_API">REST API</a> is doing its best to totally confuse me. I tend to find that if I write and do, then things become clearer.

<a href="http://stackoverflow.com/questions/22676924/how-to-construct-image-url-from-axomic-openasset-rest-api" title="How to construct image url from Axomic OpenAsset REST API">Stack overflow</a> only has one question about this particular API, and I asked it... and answered it[1. after getting a very helpful reply to an email that I sent to Axomic help]. The idea of this post is to document the steps I've gone through to try to solve the problem so that it is easier for someone who knows what they are doing to fill in the gaps in my knowledge!
<h3>My goal</h3>
<blockquote>
I want to be able to go to a specific project, and then ask that project to give me its <a href="http://help.axomic.com/05_Manage/02_Projects#Hero_Image" title="the axomic docs">hero image</a>
</blockquote>

That's the short term goal, I'm sure I'll want to do more in the future, but here's my attempts to solve _that_ problem.<br />


This is a simple ruby file that will send GET requests to an OA server[1. You don't need to be told to put _your_ details in to the top bit do you?].

<script src="https://gist.github.com/notionparallax/48c6c68577b17c95c0e5.js"></script>

This is asking for file number 2 from the general array of files. They don't seem to be in any sort of order that could be used to one's advantage.
```json
{
  "copyright_holder_id": "0",
  "photographer_id": "2",
  "original_filename": "S051205_Bluestone_004_Browell.tif",
  "download_count": "0",
  "contains_video": "0",
  "md5_now": "",
  "category_id": "1",
  "caption": "Bligh Voller 4",
  "md5_at_upload": "f37958f1c80b67ae64f527b67b528bf9",
  "id": "2",
  "project_id": "360",
  "click_count": "1",
  "rotation_since_upload": "0",
  "alternate_store_id": "0",
  "duration": "0",
  "description": "Bligh Voller 4",
  "created": "20070220133816",
  "uploaded": "20101202061904",
  "filename": "S051205_N1.tif",
  "contains_audio": "0",
  "access_level": "2",
  "user_id": "12",
  "rank": "5"
}
```

Maybe this is something to come back to.

The most obvious way to get to files related to a project is through the projects:
```request  = "/REST/1/Projects/2"```

which gives:
```json
{
 "name": "Monash University Frankston Campus",
 "name_alias_1": "",
 "code_alias_1": "",
 "name_alias_2": "",
 "id": "2",
 "alive": "1",
 "code_alias_2": "",
 "code": "M020707"
}```

but from projects there's nowhere to go!
##### Nested Resources
* Albums
  * Files
  * Groups
  * Users
* Files
  * Fields
  * Keywords
  * Sizes
* Projects
  * ProjectKeywords
  * Fields
* Fields
  * FieldLookupStrings
* Searches
  * Groups
  * Results
  * Users

`Projects` doesn't have any sub-properties that would be useful. For some reason (maybe it's the OA way) our `Projects` have the same content as our `Albums` as far as I can see. so if I ask for:
```request  = "/REST/1/Albums/384/"```

I get:
```json
{
  "private_image_count": "104,0,0,0",
  "public_image_count": "17,0,0,0",
  "company_album": "0",
  "updated": "20121004164442",
  "id": "384",
  "code": "faad6f4a48ad0dd5345c045e459f7d2a",
  "share_with_all_users": "1",
  "can_modify": 0,
  "locked": "0",
  "all_users_can_modify": "0",
  "name": "Robina Hospital Expansion",
  "description": "B0712003",
  "created": "20121004162913",
  "my_album": 0,
  "shared_album": 1,
  "user_id": "30",
  "unapproved_image_count": "0,0,0,0"
}
```

which is promising. The Nested Resources list above says that `Albums` have `Files`. But for `request = "/REST/1/Albums/384/Files"` I get
```json
{
  "error_message": "Not a valid URL.",
  "http_status_code": "400"
}```

which is a bit confusing(!) and for `request = "/REST/1/Albums/384/files"` (f not F):
```json
{
  "error_message": "Cannot create requested REST module /REST/1/Albums/384/files",
  "http_status_code": "404"
}```

So that seems like a bit of a dead end.

For the sake of completeness:

```ruby
resourses = ["AccessLevel", "Albums", "AlternateStores", "AspectRatios", "Categories", "CopyrightHolders", "CopyrightPolicies", "Fields", "Files", "Groups", "Keywords", "KeywordCategories", "Photographers", "Projects", "ProjectKeywords", "ProjectKeywordCategories", "Searches", "Sizes", "TextRewrites", "Users"]

resourses.each{|r|
    ask_oa(request+r, baseURL, params, username, password)
}
```

gives the <a href="http://notionparallax.co.uk/wordpress/wp-content/uploads/2014/07/OA_REST.txt">outcome here</a>.

[^1]: after getting a very helpful reply to an email that I sent to Axomic help

[^2]: You don't need to be told to put _your_ details in to the top bit do you?
