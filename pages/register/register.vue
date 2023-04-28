<template>
	<view>
		<swiper indicator-color="white" autoplay interval="2000" circular>
			<swiper-item>
				<image src="/static/swiper/icon.png"></image>
			</swiper-item>
		</swiper>
		<text>Username:</text>
		<input @blur="doInput(user_name)" type="number" v-model="user_name" placeholder="Enter your student id"
			maxlength="12" />
		<text>Password:</text>
		<input @blur="doInputpassword(password)" type="text" value="" v-model="password"
			placeholder="Enter your password" maxlength="16" />
		<button type="default" @tap="finishregister">Regist</button>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				user_name: "",
				password: "",
				testname: 1,
				testpassword: 1,
			}
		},
		methods: {
			doInput(val) {
				var studentID = (/^\d{12}$/)
				if (!studentID.test(val)) {
					this.testname = 1
					uni.showToast({
						title: 'User name must be 12 digits',
						icon: 'none'
					});
					return;
				}
				if (studentID.test(val)) {
					this.testname = 0
					uni.showToast({
						title: 'User name correct',
						icon: 'none'
					});
					return;
				}
			},
			doInputpassword(val) {
				if (val == "") {
					this.testpassword = 1
					uni.showToast({
						title: 'Password can not be empty',
						icon: 'none',
						position: 'bottom'
					});
					return;
				}
				if (val !== "") {
					this.testpassword = 0
					return;
				}
			},
			finishregister() {
				if (this.testname == 1) {
					uni.showToast({
						title: 'User name must be 12 digits',
						icon: 'none'
					});
					return;
				}
				if (this.testpassword == 1) {
					uni.showToast({
						title: 'Password can not be empty',
						icon: 'none',
						position: 'bottom'
					});
					return;
				}
				if (this.testname == 0 && this.testpassword == 0) {
					console.log("correct format")
					uniCloud.callFunction({
						name: "register",
						data: {
							user_name: this.user_name,
							password: this.password
						},
						success: (res) => {
							console.log(res)
							let status = res.result.status
							if (status == 0) {
								uni.showToast({
									title: 'Register successfully!',
									icon: 'none',
									position: 'bottom'
								})
								uni.navigateTo({
									url: "../login/login"
								})
							}
							if (status == 1) {
								uni.showToast({
									title: 'Already have this user!',
									icon: 'none',
									position: 'bottom'
								})
							}
						}
					})
				}
				if (this.testname == 0 && this.testpassword == 0) {
					console.log("correct format")
					uniCloud.callFunction({
						name: "adduserinfo",
						data: {
							user_name: this.user_name,
							studentID:"",
							gender:"",
							class:"",
							chinese_name:"",
							english_name:"",
							subject:"",
							student_email:"",
							telephone:""
							
						},
						success: (res) => {
							console.log(res)
						}
					})
				}
			}
		}
	}
</script>

<style>
	swiper image {
		width: 100%;
		height: 100%;
	}

	input {
		border: 1upx solid #dadbde;
		padding: 12upx 18upx;
		border-radius: 8upx;
		font-size: 30upx;
		color: rgb(48, 49, 51);
	}
</style>