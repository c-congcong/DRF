from rest_framework import serializers, exceptions

from app_day3_lx.models import Book, Press


class PressModelSerializer(serializers.ModelSerializer):


    class Meta:
        model = Press
        fields = ("press_name", "address", "pic")


class BookModelSerializer(serializers.ModelSerializer):

    publish = PressModelSerializer()

    class Meta:
        model = Book
        fields = ("book_name", "price", "pic", "publish")

        # 可以直接查询所有字段
        # fields = "__all__"

        # 可以指定不展示哪些字段
        # exclude = ("is_delete", "create_time", "status")

        # 指定查询深度  关联对象的查询  可以查询出有外键关系的信息
        # depth = 1


class BookDeModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ("book_name", "price", "publish", "authors")

        # 添加DRF所提供的校验规
        extra_kwargs = {
            "book_name": {
                "required": True,
                "min_length": 5,
                "error_messages": {
                    "required": "图书名是必填的",
                    "min_length": "图书名长度不够"
                }
            },
            "price": {
                "max_digits": 5,
                "decimal_places": 4,
            }
        }

    def validate_book_name(self, value):
        if "1" in value:
            raise exceptions.ValidationError("图书名含有敏感字")
        return value

    # 全局校验钩子
    def validate(self, attrs):
        pwd = attrs.get("password")
        re_pwd = attrs.pop("re_pwd")
        if pwd != re_pwd:
            raise exceptions.ValidationError("两次密码不一致")

        return attrs


class BookModelSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("book_name", "price", "publish", "authors", "pic")

        extra_kwargs = {
            "book_name": {
                "required": True,
                "min_length": 3,
                "error_messages": {
                    "required": "图书名是必填的",
                    "min_length": "长度不够，太短啦~"
                }
            },
            "publish": {
                "write_only": True
            },
            "authors": {
                "write_only": True
            },
            "pic": {
                "read_only": True
            }
        }

    def validate_book_name(self, value):
        if "1" in value:
            raise exceptions.ValidationError("图书名含有敏感字")
        return value

    # 全局校验钩子
    def validate(self, attrs):

        price = attrs.get("price", 0)
        if price > 90:
            raise exceptions.ValidationError("超过设定的最高价钱")

        return attrs
