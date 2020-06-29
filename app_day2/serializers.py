from rest_framework import serializers

from app.models import Students


class StudentsSerializer(serializers.Serializer):
    st_name = serializers.CharField()
    age = serializers.CharField()
    st_id = serializers.CharField()

    salt = serializers.SerializerMethodField()

    def get_salt(self, obj):
        return "salt"

    gender = serializers.SerializerMethodField()

    def get_gender(self, obj):
        return obj.get_gender_display()


class StudentsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ("st_name", "age", "st_id", "gender")
        extra_kwargs = {
            "st_name": {
                "required": True,
                "min_length": 2,
                "error_messages": {
                    "required": "学生名字是必填的",
                    "min_length": "学生名长度太短"
                }
            },
            "st_id": {
                "required": True,
                "min_length": 12,
                "error_messages": {
                    "required": "学号是必填的",
                    "min_length": "学号长度必须为12位"
                }
            },
        }

    def validate_age(self, value):
        if value > 99:
            raise serializers.ValidationError("神仙？")
        else:
            return value

    def validate(self, attrs):
        stid = attrs.get("st_id")
        print(stid)
        st_obj = Students.objects.filter(st_id=stid)
        if st_obj:
            raise serializers.ValidationError("学号重复")

        return attrs
