import string
from django.core.exceptions import ValidationError


def contains_special_character(value):
    for char in value:
        if char in string.punctuation: #string.punctuation: 특수문자열 모음
            return True
    return False


# 실습으로 완성해 주세요
def contains_uppercase_letter(value):
    for i in value:
        if i.isupper():
            return True
    return False


# 실습으로 완성해 주세요
def contains_lowercase_letter(value):
    for i in value:
        if i.islower():
            return True
    return False


# 실습으로 완성해 주세요
def contains_number(value):
    for i in value:
        if i.isdigit():
            return True
    return False


class CustomPasswordValidator:
    def validate(self, password, user=None):
        if (
                len(password) < 8 or
                not contains_uppercase_letter(password) or
                not contains_lowercase_letter(password) or
                not contains_number(password) or
                not contains_special_character(password)
        ):
            raise ValidationError("8자 이상의 영문 대/소문자, 숫자, 특수문자 조합이어야 합니다.")

    def get_help_text(self): #어드민페이지에서 비밀번호 바꿀 때 필요한 내용
        return "8자 이상의 영문 대/소문자, 숫자, 특수문자 조합을 입력해 주세요."
        

def validate_no_special_characters(value):
    if contains_special_character(value):
        raise ValidationError("특수문자를 포함할 수 없습니다.")
        

    
    
def validate_retaurant_link(value):
    if "place.naver.com" not in value and "place.map.kakao.com" not in value:
        raise ValidationError("place.naver.com 또는 place.map.kakao.com이 들어가야 합니다.")