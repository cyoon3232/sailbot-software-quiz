from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_boundaries():
    assert bound_to_180(0) == 0.0
    assert bound_to_180(-180) == -180.0
    assert bound_to_180(180) == -180.0
    assert bound_to_180(360) == 0.0


def test_bound_angles_in_range():
    assert bound_to_180(20) == 20.0
    assert bound_to_180(135) == 135.0
    assert bound_to_180(-135) == -135.0


def test_bound_angles_out_of_range():
    assert bound_to_180(200) == -160.0
    assert bound_to_180(-200) == 160.0


def test_bound_angles_after_360():
    assert bound_to_180(380) == 20.0
    assert bound_to_180(-380) == -20.0
    assert bound_to_180(-910) == 170.0


""" Tests for is_angle_between() """


def test_between_basics():
    assert is_angle_between(0, 1, 2)
    assert is_angle_between(0, 45, 90)
    assert not is_angle_between(45, 90, 270)
    assert not is_angle_between(-45, -90, -270)
    assert is_angle_between(340, 750, 40)
    assert not is_angle_between(380, 700, 40)


def test_between_when_bounds_are_equal():
    assert is_angle_between(0, 0, 0)
    assert is_angle_between(0, 0, 360)


def test_between_when_middle_equal_boundes():
    assert is_angle_between(0, 0, 90)
    assert is_angle_between(0, 90, 90)


def test_between_when_bounds_are_180():
    assert is_angle_between(0, 90, 180)
    assert is_angle_between(0, -90, 180)
