from cs_fields import CSField

class Mentee:
    def __init__(self) -> None:
        self.name: str = ""
        self.email: str = ""
        self.pronouns = None
        self.university = None
        self.degree = None
        self.intended_field: CSField = CSField.COMPILERS
        self.degree_type = None
        self.research_areas = []
        self.professor_ranking = []
        self.assistance_categories = []

        self.mentor_ranking_list: list["Mentor"] = []
        self.current_mentor_index = 0
        self.assigned_mentor = None

    def __hash__(self):
        return hash(self.email)

    def __eq__(self, value: "Mentee") -> bool:  # type: ignore
        if not isinstance(value, Mentee):
            return False

        return self.email == value.email

    def rank_mentors(self, mentors: list["Mentor"]):
        self.mentor_ranking_list = list(
            sorted(mentors, key=lambda m: match_score(m, self), reverse=True)
        )

    def find_mentor(self):
        while not self.has_mentor() and self.current_mentor_index < len(
            self.mentor_ranking_list
        ):
            mentor = self.mentor_ranking_list[self.current_mentor_index]
            self.current_mentor_index += 1
            mentor.try_assign_mentee(self)

        return self.has_mentor()

    def assign_mentor(self, mentor: "Mentor"):
        assert self.assigned_mentor is None

        self.assigned_mentor = mentor

    def evict_mentor(self):
        self.assigned_mentor = None

    def has_mentor(self):
        return self.assigned_mentor is not None


class Mentor:
    def __init__(self) -> None:
        self.name = ""
        self.advisor = None
        self.email = None
        self.research_field = None
        self.background = []
        self.assistance_categories = []
        self.availability_capacity = 0
        self.mentee_count = 0
        self.mentee_ranking_list: list[Mentee] = []
        self.assigned_mentees: list[Mentee] = []

    def rank_mentees(self, mentees: list[Mentee]):
        self.mentee_ranking_list = list(
            sorted(mentees, key=lambda m: match_score(self, m), reverse=True)
        )

    def try_assign_mentee(self, mentee: Mentee):
        assert mentee.email not in map(lambda m: m.email, self.assigned_mentees)

        if self.mentee_count < self.availability_capacity:
            self.mentee_count += 1
            self.assigned_mentees.append(mentee)
            mentee.assign_mentor(self)
            return

        last_mentee = max(self.assigned_mentees, key=lambda m: self.mentee_ranking_list.index(m))
        mentee_ranking = self.mentee_ranking_list.index(mentee)

        if self.mentee_ranking_list.index(last_mentee) < mentee_ranking:
            return

        evicted_mentee = self.assigned_mentees.pop(self.assigned_mentees.index(last_mentee))
        evicted_mentee.evict_mentor()

        self.assigned_mentees.append(mentee)
        mentee.assign_mentor(self)
        return


def match_score(mentor: Mentor, mentee: Mentee):
    # The faculty score indicates how mentor's advisor ranks in the mentee's
    # faculty ranking list. It is 0 if the advisor is not ranked at all.
    try:
        faculty_rank_index = mentee.professor_ranking.index(mentor.advisor)

        # we invert this score such that higher value means better.
        faculty_score = 1 - faculty_rank_index / len(mentee.professor_ranking)
    except ValueError:
        faculty_score = 0

    # The assistance type score is the Jaccard Overlap between the mentor
    # and mentee assistance type categories.
    category_union = set(mentor.assistance_categories) | set(
        mentee.assistance_categories
    )
    category_intersection = set(mentor.assistance_categories) & set(
        mentee.assistance_categories
    )
    assistance_type_score = len(category_intersection) / len(category_union)

    # The availability score is the percentage of time the mentor would spend
    # each with mentee if all slots are full
    availability_score = 1 / (mentor.availability_capacity)

    return 0.4 * faculty_score + 0.1 * assistance_type_score + 0.1 * availability_score


def stable_match(mentors: list[Mentor], mentees: list[Mentee]):

    for m in mentors:
        m.rank_mentees(mentees)
    for m in mentees:
        m.rank_mentors(mentors)

    hasChanges = True
    while hasChanges:
        hasChanges = False
        for m in mentees:
            if m.has_mentor():
                continue

            if m.find_mentor():
                hasChanges = True
