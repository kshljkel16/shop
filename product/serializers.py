from rest_framework import serializers
from .models import Product, ProductReview

class ProductListSerializer(serializers.ModelSerializer):
    """
    Класс для перевода типов данных ПИТОН в ЖЕЙСОН формат
    """
    # total_sum = serializers.DecimalField() #доп поле<

    class Meta:
        """
        Класс для передачи дополнительных данных
        """
        model = Product
        exclude = ("description","image","created_at")
        # fields = "__all__"
        # fiels = ("title","status","description","price","image","total_sum)

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        representation = super(ProductDetailSerializer, self).to_representation(instance)
        representation['reviews'] = ProductReviewSerializer(
            ProductReview.objects.filter(product=instance.id),
            many=True
        ).data
        return representation

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta(ProductDetailSerializer.Meta):
        pass
    def validate_price(self,price):
        if price < 100:
            raise serializers.ValidationError(
                "Цена не может быть - и <0"
            )
        return price

class ProductReviewSerializer(serializers.ModelSerializer):
    product_title = serializers.SerializerMethodField("get_product_title")
    class Meta:
        model = ProductReview
        fields = "__all__"

    def get_product_title(self, product_review):
        title = product_review.product.title
        return title

    def validate_product(self,product):
        if self.Meta.model.objects.filter(product=product).exists():
            raise serializers.ValidationError(
                "Вы уже оставляли отзыв на данный продукт"
            )
        return product

    def validate_rating(self, rating):
        if rating not in range(1,6):
            raise serializers.ValidationError(
                "рейтинг дрлжен быть от 1 до 5"
            )
        return rating

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        print(request, 'HELLLLLLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')

        if not request.user.is_anonymous:
            representation['author'] = request.user.email
        return representation

