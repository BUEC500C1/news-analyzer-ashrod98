# unit test for newsfeed search module

# sunny day, not representative of NYTAPI, uses goodgle search 
test_input : {
    (["superbowl"], 5, 'pub_year': '2021')
}

expected_output : {
    [
        "Article" : {
            "File_Name" : 'The Path Back to the Super Bowl for the Kansas City Chiefs'
            "File_URI" : 'https://www.si.com/nfl/chiefs/gm-report/the-path-back-to-the-super-bowl-for-the-kansas-city-chiefs'
            "File_Type" : 'URL'
            "Metadata" : {
                "Author" : 'Mark Van Sickle'
                "Published_At" : '2021-02-20'
                "Source" : {
                    "Source" : 'news analyzer'
                    "Search_param" : ["superbowl"]
                    "Filters" : ['pub_year': '2021']
                }
        }
        "Article" : {
            "File_Name" : 'Luke Bryan Texted Eric Church After 2021 Super Bowl Anthem'
            "File_URI" : 'https://tasteofcountry.com/luke-bryan-texted-eric-church-2021-super-bowl-national-anthem/'
            "File_Type" : 'URL'
            "Metadata" : {
                "Author" : 'Sterling Whitaker'
                "Published_At" : '2021-02-20'
                "Source" : {
                    "Source" : 'news analyzer'
                    "Search_param" : ["superbowl"]
                    "Filters" : ['pub_year': '2021']
                }
            }
        }
        "Article" : {
            "File_Name" : 'Leonard Fournette Credits Tom Brady\'s Pregame Speech for Bucs\' Super Bowl Win: \'It Woke Us Up\''
            "File_URI" : 'https://www.si.com/nfl/2021/02/19/leonard-fournette-tom-brady-buccaneers-super-bowl-speech'
            "File_Type" : 'URL'
            "Metadata" : {
                "Author" : 'Wilton Jackson'
                "Published_At" : '2021-01-19'
                "Source" : {
                    "Source" : 'news analyzer'
                    "Search_param" : ["superbowl"]
                    "Filters" : ['pub_year': '2021']
                }
            }
        }
        "Article" : {
            "File_Name" : 'WATCH: Patrick Mahomes, Travis Kelce mic\'d up for Super Bowl LV vs. Buccaneers'
            "File_URI" : 'https://chiefswire.usatoday.com/2021/02/19/kansas-city-chiefs-patrick-mahomes-travis-kelce-micd-up-super-bowl-55/'
            "File_Type" : 'URL'
            "Metadata" : {
                "Author" : 'Charles Goldman'
                "Published_At" : '2021-02-19'
                "Source" : {
                    "Source" : 'news analyzer'
                    "Search_param" : ["superbowl"]
                    "Filters" : ['pub_year': '2021']
                }
            }
        }
        "Article" : {
            "File_Name" : 'Tom Brady gave Buccaneers speech ‘we all needed to hear’ before Super Bowl LV, per Leonard Fournette'
            "File_URI" : 'https://www.masslive.com/patriots/2021/02/tom-brady-gave-buccaneers-speech-we-all-needed-to-hear-before-super-bowl-lv-per-leonard-fournette.html'
            "File_Type" : 'URL'
            "Metadata" : {
                "Author" : 'Chris Mason'
                "Published_At" : '2021-02-19'
                "Source" : {
                    "Source" : 'news analyzer'
                    "Search_param" : ["superbowl"]
                    "Filters" : ['pub_year': '2021']
                }
            }
        }
    ]
}

