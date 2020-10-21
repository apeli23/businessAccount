
		
	# 	if income.is_valid():
	# 		income.save()
	# 		income =  income.cleaned_data["unit_price"]
	# 		income = incomeForm()
	# 		return redirect('/income/')

	# 	args = {"form":form, "unit_price":unit_price}
	# 	return render(request, self.template_name, args)

	# def post(self, request, *args, **kwargs):
	# 	try:
	# 		income = incomeForm(request.POST)
	# 		Transactions.objects.create(
	# 			unit_price = income.data['unit_price'],

	# 		)

	# 		context = {
	# 			"Message": "Success",
	# 			"Success": True
	# 			}
	# 		except Exception as e:
	# 			context = {
 #                "Message": str(e),
 #                "Success": False
 #            }

        # this should re