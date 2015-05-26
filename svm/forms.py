from django import forms

class ApplicationForm(forms.Form):
    PARENTS_CHOICES = (
            ('usual', 'Usual'),
            ('pretentious', 'Pretentious'),
            ('great_pret', 'Great Pretentious'),
        )
    HAS_NURS_CHOICES = (
            ('proper', 'Proper'),
            ('less_proper', 'Less Proper'),
            ('improper', 'Improper'),
            ('critical', 'Critical'),
            ('very_crit','Very Critical')
        )
    FORM_CHOICES = (
            ('complete', 'Complete'),
            ('completed', 'Completed'),
            ('incomplete', 'Incomplete'),
            ('foster', 'Foster'),
        )
    CHILDREN_CHOICES = (
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('more', 'More')
        )
    HOUSING_CHOICES = (
            ('convenient', 'Convenient'),
            ('less_conv', 'Less Convenient'),
            ('critical','Critical')
        )
    FINANCE_CHOICES = (
            ('convenient', 'Convenient'),
            ('inconv', 'Inconvenient'),
        )
    SOCIAL_CHOICES = (
            ('nonprob', 'Non-problematic'),
            ('slightly_prob', 'Slightly problematic'),
            ('problematic', 'Problematic'),
        )
    HEALTH_CHOICES = (
            ('recommended', 'Recommended'),
            ('priority', 'Priority'),
            ('not_recom', 'Not Recommended'),
        )
    parents = forms.ChoiceField(
        choices=PARENTS_CHOICES, widget=forms.RadioSelect(attrs={'class':'radio'}),
        label='Parent\'s Occupation', help_text='PRETENTIOUS - irregular job; GREAT PRETENTIOUS - doesn\'t have a job; USUAL - has a regular job ')
    has_nurs = forms.ChoiceField(
        choices=HAS_NURS_CHOICES, widget=forms.RadioSelect(attrs={'class':'radio'}),
        label='Child\'s Nursery', help_text='CRITICAL - a nursery with disappointing comments from parents/children; VERY CRITICAL - a nursery with very disappointing reputation; LESS PROPER - nursery with less facilities; PROPER - nursery with complete facilites, good reputation, has license; IMPROPER - nursery doesn\'t have permanent staff, incomplete facilities')
    form = forms.ChoiceField(
        choices=FORM_CHOICES, widget=forms.RadioSelect(attrs={'class':'radio'}),
        label='Form of the Family', help_text='INCOMPLETE - child was raised by either of his/her mother/father; FOSTER - child is adopted; COMPLETED - child\'s mother/father is deceased; COMPLETE - child has mother and father')
    children = forms.ChoiceField(
        choices=CHILDREN_CHOICES, widget=forms.RadioSelect(attrs={'class':'radio'}),
        label='Number of Children', help_text='1 - only child; 2 - two children; 3 - three children; MORE - four or more children')
    housing = forms.ChoiceField(
        choices=HOUSING_CHOICES, widget=forms.RadioSelect(attrs={'class':'radio'}),
        label='Housing Conditions', help_text='CRITICAL - lives in a squatter area; LESS CRITICAL - house-and-lot is rented; CONVENIENT - house and lot is owned with expensive furnitures')
    finance = forms.ChoiceField(
        choices=FINANCE_CHOICES, widget=forms.RadioSelect(attrs={'class':'radio'}),
        label='Financial Standing of the Family', help_text='INCONVENIENT - liabilities are greater than assets; CONVENIENT - assets are greater than liabilities')
    social = forms.ChoiceField(
        choices=SOCIAL_CHOICES, widget=forms.RadioSelect(attrs={'class':'radio'}),
        label='Social Conditions', help_text='PROBLEMATIC - doesn\'t have any friends; NON PROBLEMATIC - child has a lot of friends and was not bullied; SLIGHTLY PROBLEMATIC - child is moody, sometimes child doesn\'t  want to talk to other people')
    health = forms.ChoiceField(
        choices=HEALTH_CHOICES, widget=forms.RadioSelect(attrs={'class':'radio'}),
        label='Health Conditions', help_text='PRIORITY - child\'s sickness must be monitored all the time; NOT RECOMMENDED - child is healthy; RECOMMENDED - child has mild sickness')