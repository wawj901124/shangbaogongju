    # 重写formfield_for_dbfield，设计add和edit表单
    def formfield_for_dbfield(self, db_field, **kwargs):
        if not self.request.user.is_superuser:
        	# 对case这个表项的下拉框选择进行过滤
            if db_field.name == "case":
                kwargs["queryset"] = Case.objects.filter(case_owner=self.request.user).order_by('id')
            # 对assigned_recipient这个表项的下拉选择进行过滤
            # 并且需要用到外键
            if db_field.name == "assigned_recipient":
                stu_ids = StudentDoctor.objects.filter(doctor=self.request.user).values('student_id')
                ids = []
                # 这里使用循环，为了下方再次查询时在list中使用in
                for id in stu_ids:
                    ids.append(id['student_id'])
				# 根据主键在ids列表中查询得到Queryset。注意kwargs["queryset"]一定是queryset
                kwargs["queryset"] = User.objects.filter(pk__in=ids)
            return db_field.formfield(**dict(**kwargs))

        else:
            attrs = self.get_field_attrs(db_field, **kwargs)
            return db_field.formfield(**dict(attrs, **kwargs))