from django import forms

class ApplicationForm(forms.Form):
    PARENTS_CHOICES = (
            ('Usual', 'usual'),
            ('Pretentious', 'pretentious'),
            ('Great Pretentious', 'great_pret'),
        )
    HAS_NURS_CHOICES = (
            ('Proper', 'proper'),
            ('Less Proper', 'less_proper'),
            ('Improper', 'improper'),
            ('Critical', 'critical'),
            ('Very Critical', 'very_crit'),
        )
    FORM_CHOICES = (
            ('Complete', 'complete'),
            ('Completed', 'completed'),
            ('Incomplete', 'incomplete'),
            ('Foster', 'foster'),
        )
    CHILDREN_CHOICES = (
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('More', 'more')
        )
    HOUSING_CHOICES = (
            ('Convenient', 'convenient'),
            ('Less Convenient', 'less_conv'),
            ('Critical','critical')
        )
    FINANCE_CHOICES = (
            ('Convenient', 'convenient'),
            ('Inconvenient', 'inconv'),
        )
    SOCIAL_CHOICES = (
            ('Non-problematic', 'non-prob'),
            ('Slightly problematic', 'slightly_prob'),
            ('Problematic', 'problematic'),
        )
    HEALTH_CHOICES = (
            ('Recommended', 'recommended'),
            ('Priority', 'priority'),
            ('Not Recommended', 'not_recom'),
        )
    parents = forms.ChoiceField(
        choices=PARENTS_CHOICES, widget=forms.RadioSelect,
        label='Parent\'s Occupation')
    has_nurs = forms.ChoiceField(
        choices=HAS_NURS_CHOICES, widget=forms.RadioSelect,
        label='Child\'s Nursery')
    form = forms.ChoiceField(
        choices=FORM_CHOICES, widget=forms.RadioSelect,
        label='Form of the Family')
    children = forms.ChoiceField(
        choices=CHILDREN_CHOICES, widget=forms.RadioSelect,
        label='Number of Children')
    housing = forms.ChoiceField(
        choices=HOUSING_CHOICES, widget=forms.RadioSelect,
        label='Housing Conditions')
    finance = forms.ChoiceField(
        choices=HAS_NURS_CHOICES, widget=forms.RadioSelect,
        label='Financial Standing of the Family')
    social = forms.ChoiceField(
        choices=HAS_NURS_CHOICES, widget=forms.RadioSelect,
        label='Social Conditions')
    health = forms.ChoiceField(
        choices=HAS_NURS_CHOICES, widget=forms.RadioSelect,
        label='Health Conditions')

