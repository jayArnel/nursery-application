from django import forms

class ApplicationForm(forms.Form):
    PARENTS_CHOICES = (
            ('usual', 'Usual'),
            ('pretentious', 'Ppretentious'),
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

