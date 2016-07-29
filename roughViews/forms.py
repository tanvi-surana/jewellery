from django import forms

# Create your forms here

class filterForm(forms.Form):
	productChoices=(('Rings','Rings'),('Earrings','Earrings'),('Bangles','Bangles'),('Pendants','Pendants'),('Bracelets','Bracelets'),('Necklaces','Necklaces'),('Nosepins','Nosepins'),('Mangalsutras','MangalSutras'),('Chains','Chains'))
	productType=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=productChoices,label='Product Type')
	metalChoice=(('Yellow Gold','Yellow Gold'),('White Gold','White Gold'))
	netalType=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=metalChoice,label='Metal Type')
	purityChoices=(('18 kt','18 kt'),('20 kt','20 kt'),('22 kt','22 kt'),('23 kt','23 kt'))
	purity=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=purityChoices,label='Purity')
	diamondShapeChoices=(('Other','Other'),('Round','Round'),('Oval','Oval'),('Pear','Pear'),('Heart','Heart'),('Princess','Princess'),('Asscher','Asscher'),('Marquise','Marquise'),('Emerald','Emerald'),('Radiant','Radiant'),('Cushion','Cushion'))
	diamondShape=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=diamondShapeChoices,label='Diamond Shape')
