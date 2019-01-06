from django.db import models


class Robot(models.Model):
    """
    An entity that represents a single robot.
    """
    name = models.CharField(
        max_length=20,
        help_text='The robot\'s name.'
    )

    def __str__(self):
        return self.name


class RobotPart(models.Model):
    """
    An entity that represents a part that a robot is using.
    """

    FUNCTIONAL = 'F'
    DAMAGED = 'D'
    NONFUNCTIONAL = 'N'

    PART_CONDITION_CHOICES = (
        (FUNCTIONAL, 'Functional'),
        (DAMAGED, 'Damaged'),
        (NONFUNCTIONAL, 'Nonfunctional'),
    )

    condition = models.CharField(
        max_length=1,
        choices=PART_CONDITION_CHOICES,
        default=FUNCTIONAL
    )

    robot = models.ForeignKey(
        'robots.Robot',
        related_name='robot_parts',
        on_delete=models.CASCADE,
        help_text='The robot this part belongs to.'
    )

    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        help_text='The product for this robot part.'
    )
