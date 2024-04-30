class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)


    class Meta:
        model=User
        fields = ['other_names', 'last_name', 'email', 'mobile_phone', 'username', 'role', 'password1', 'password2']

        def validate(self, data):
            if data['password1'] != data['password2']:
                raise serializers.ValidationError("Passwords do not match")
            return data
        
        def create(seld, validated_data):
            validated_data.pop('password2')
            password = validated_data.pop('password1')
            user = User.objects.create(**validated_data)
            user.set_password(password)
            user.save()
            return user
        