from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts
 
TEXT = '''
You know the day destroys the night
Night divides the day
Tried to run
Tried to hide
Break on through to the other side
Break on through to the other side
Break on through to the other side, yeah
 
We chased our pleasures here
Dug our treasures there
But can you still recall
The time we cried
Break on through to the other side
Break on through to the other side
Yeah!
C'mon, yeah
Everybody loves my baby
Everybody loves my baby
She get
She get
She get
She get high
I found an island in your arms
Country in your eyes
Arms that chain us
Eyes that lie
Break on through to the other side
Break on through to the other side
Break on through, oww!
Oh, yeah!
Made the scene
Week to week
Day to day
Hour to hour
The gate is straight
Deep and wide
Break on through to the other side
Break on through to the other side
Break on through
Break on through
Break on through
Break on through
Yeah, yeah, yeah, yeah
Yeah, yeah, yeah, yeah, yeah'''
 
tags = make_tags(get_tag_counts(TEXT), maxsize=150)

create_tag_image(tags, 'cloud_large.png', size=(900, 600))