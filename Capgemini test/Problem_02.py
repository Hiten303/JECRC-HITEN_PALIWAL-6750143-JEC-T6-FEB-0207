class Solution:

    def subject_average(self, students):
        subject_total = {}
        subject_count = {}
        ## Write your code here and don't forget to add return keyword

        for student in students:
            marks = student["marks"]

            for subject, score in marks.items():
                if subject in subject_total:
                    subject_total[subject]+=score
                    subject_count[subject]+=1

                else:
                    subject_total[subject]=score
                    subject_count[subject]=1

        subject_average = {}
        for subject in subject_total:
            subject_average[subject]=subject_total[subject]/subject_count[subject]

        top_subject = max(subject_average, key=subject_average.get)
        return [subject_average, top_subject]
        