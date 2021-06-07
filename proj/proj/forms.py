# Form 1: Name: People; Purpose: Collect basic demographic information;
# Visible Fields: First and Last Name, DOB, Age, Gender
# Hidden Fields: Participant ID

# Form 2: Name: Practice; Purpose: Collect practice trial data;
# Visible Fields: Player 1, Player 2, Behavior
# Hidden Fields: None

# Form 3: Name: Game Round 1; Purpose: Collect test trial data on each round of the game;
# Visible Fields: Answer 1, Answer 2
# Hidden Fields: None

# Form 4: Name: Game Round 2; Purpose: Collect test trial data on each round of the game;
# Visible Fields: Player 1, Player 2, Behavior 2
# Hidden Fields: None

# Form 5: Name: Game Round 3; Purpose: Collect test trial data on each round of the game;
# Visible Fields: Player 1, Player 2, Behavior 3
# Hidden Fields: None

# Form 6: Name: Game Round 4; Purpose: Collect test trial data on each round of the game;
# Visible Fields: Player 1, Player 2, Behavior 4
# Hidden Fields: None

from django.forms import ModelForm, modelformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from proj.models import Person, Practice, Round
from django.core.exceptions import ValidationError

# define person form
class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)

        # Crispy forms stuff
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

# define practice round 1 form
class Practice1Form(ModelForm):
    class Meta:
        model = Practice
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Practice1Form, self).__init__(*args, **kwargs)
        self.fields['answer'].label = ''

        # Crispy forms stuff
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    # Validation: Make sure that choice 2 is picked
    def clean(self):
        cleaned_data = super().clean()

        practice = cleaned_data.get("answer")
        if practice == 1 or 3 or 4:
            raise ValidationError(
                "Oops! That is not the right answer! Please try again. Click 'Instructions' to view rules again."
            )

# define practice round 2 form
class Practice2Form(ModelForm):
    class Meta:
        model = Practice
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Practice2Form, self).__init__(*args, **kwargs)
        self.fields['answer'].label = ''

        # Crispy forms stuff
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    # Validation: Make sure that choice 1 is picked
    def clean(self):
        cleaned_data = super().clean()

        practice = cleaned_data.get("answer")
        if practice == 2 or 3 or 4:
            raise ValidationError(
                "Oops! That is not the right answer! Please try again. Click 'Instructions' to view rules again."
            )

# define practice round 3 form
class Practice3Form(ModelForm):
    class Meta:
        model = Practice
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Practice3Form, self).__init__(*args, **kwargs)
        self.fields['answer'].label = ''

        # Crispy forms stuff
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    # Validation: Make sure that choice 3 is picked
    def clean(self):
        cleaned_data = super().clean()

        practice = cleaned_data.get("answer")
        if practice == 1 or 2 or 4:
            raise ValidationError(
                "Oops! That is not the right answer! Please try again. Click 'Instructions' to view rules again."
            )

# define practice round 4 form
class Practice4Form(ModelForm):
    class Meta:
        model = Practice
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Practice4Form, self).__init__(*args, **kwargs)
        self.fields['answer'].label = ''

        # Crispy forms stuff
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    # Validation: Make sure that choice 4 is picked
    def clean(self):
        cleaned_data = super().clean()

        practice = cleaned_data.get("answer")
        if practice == 1 or 2 or 3:
            raise ValidationError(
                "Oops! That is not the right answer! Please try again. Click 'Instructions' to view rules again."
            )

# define game round 1 form
class Observation1Form(ModelForm):
    class Meta:
        model = Round
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Observation1Form, self).__init__(*args, **kwargs)
        self.fields['choice'].label = 'Round 1 starts now. Which card would you choose?'

        # Crispy forms stuff
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

# define game round 2 form
class Observation2Form(ModelForm):
    class Meta:
        model = Round
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Observation2Form, self).__init__(*args, **kwargs)
        self.fields['choice'].label = 'Round 2 starts now. Which card would you choose?'

        # Crispy forms stuff
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

# define game round 3 form
class Observation3Form(ModelForm):
    class Meta:
        model = Round
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Observation3Form, self).__init__(*args, **kwargs)
        self.fields['choice'].label = 'Round 3 starts now. Which card would you choose?'

        # Crispy forms stuff
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

# define game round 4 form
class Observation4Form(ModelForm):
    class Meta:
        model = Round
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Observation4Form, self).__init__(*args, **kwargs)
        self.fields['choice'].label = 'Round 4 starts now. Which card would you choose?'

        # Crispy forms stuff
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))


Practice1ModelFormSet = modelformset_factory(Practice, form=Practice1Form, extra=0, max_num=1)
Practice2ModelFormSet = modelformset_factory(Practice, form=Practice2Form, extra=0, max_num=1)
Practice3ModelFormSet = modelformset_factory(Practice, form=Practice3Form, extra=0, max_num=1)
Practice4ModelFormSet = modelformset_factory(Practice, form=Practice4Form, extra=0, max_num=1)


Observation1ModelFormSet = modelformset_factory(Round, form=Observation1Form, extra=0, max_num=1)
Observation2ModelFormSet = modelformset_factory(Round, form=Observation2Form, extra=0, max_num=1)
Observation3ModelFormSet = modelformset_factory(Round, form=Observation3Form, extra=0, max_num=1)
Observation4ModelFormSet = modelformset_factory(Round, form=Observation4Form, extra=0, max_num=1)