<template>
	<view class="item">
		<swiper indicator-color="white" autoplay interval="2000" circular>
			<swiper-item>
				<image src="/static/swiper/icon.png"></image>
			</swiper-item>
		</swiper>
		<view class="loginput">
			<view class="username">
				<text>Username:</text>
				<input @blur="doInput(user_name)" type="number" value="" v-model="user_name"
					placeholder="Enter your student id" maxlength="12" />
			</view>
			<view class="userpassword">
				<text>Password:</text>
				<input @blur="doInputpassword(password)" type="text" password="true" value="" v-model="password"
					placeholder="Enter your password" maxlength="16" />
			</view>
		</view>
		<view class="buttons">
			<button type="primary" class="btlogin" @tap="login()">Login</button>
			<button type="default" class="btregister" @tap="register()">Regist</button>
		</view>
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
						title: 'User name error',
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
			login() {
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
					let users = {
						user_name: this.user_name,
						password: this.password
					}
					uniCloud.callFunction({
						name: "login",
						data: users,
						success: (res) => {
							console.log(res)
							let status = res.result.status
							this.user_name = res.result.user_name
							this.id = res.result.id
							if (status == 0) {
								uni.showToast({
									title: 'Login successfully!',
									icon: 'none',
									position: 'bottom'
								})
								uni.setStorageSync('user_name',this.user_name)
								uni.redirectTo({
									url: "../userInfo/userInfo?user_name=" + this.user_name
								})
							} else if (status == 1) {
								uni.showToast({
									title: 'No this User!',
									icon: 'none',
									position: 'bottom'
								})

							} else if (status == 2) {
								uni.showToast({
									title: 'Password wrong!',
									icon: 'none',
									position: 'bottom'
								})

							}
						}
					})
				}
			},
			register() {
				uni.navigateTo({
					url: "../register/register"
				})
			}
		},
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