<template>
	<view>
		<text class="title">personal information</text>
		<view class="menu" v-for="(item,index) in list">
			<button @tap="">
				<view class="menu-item">
					<view v-model="user_name">User:<text class="con"> {{user_name}}</text></view>
				</view>
			</button>
			<button @tap="StudentID()">
				<view class="menu-item">
					<view v-model="studentID">StudentID:<text class="con"> {{item.studentID}}</text></view>
				</view>
			</button>
			<button @tap="Gender()">
				<view class="menu-item">
					<view>Gender:<text class="con"> {{item.gender}}</text></view>
				</view>
			</button>
			<button @tap="Class()">
				<view class="menu-item">
					<view>Class:<text class="con"> {{item.class}}</text></view>
				</view>
			</button>
			<button @tap="ChineseName()">
				<view class="menu-item">
					<view>Chinese name:<text class="con">{{item.chinese_name}}</text></view>
				</view>
			</button>
			<button @tap="EnglishName()">
				<view class="menu-item">
					<view>English name:<text class="con">{{item.english_name}}</text></view>
				</view>
			</button>
			<button @tap="Subject()">
				<view class="menu-item">
					<view>Specialized subject:<text class="con">{{item.subject}}</text></view>
				</view>
			</button>
			<button @tap="Email()">
				<view class="menu-item">
					<view>Email:<text class="con">{{item.student_email}}</text></view>
				</view>
			</button>
			<button @tap="Telephone()">
				<view class="menu-item">
					<view>telephone:<text class="con">{{item.telephone}}</text></view>
				</view>
			</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				list: [],
				user_name: "",
			};
		},
		onLoad(event) {
			if (!uni.getStorageSync('user_name')) {
				uni.showToast({
					title: 'Please login!',
					icon: 'error'
				})
				uni.navigateTo({
					url: '/pages/login/login'
				})
			}
			this.user_name = uni.getStorageSync('user_name');
		},
		onShow() {
			this.getinfo()
		},
		methods: {
			StudentID() {
				let that = this;
				uni.showModal({
					title: 'edit student ID',
					editable: true,
					success: function(res) {
						if (res.confirm) {
							console.log('edit studentID')
							uniCloud.callFunction({
								name: 'editstudentID',
								data: {
									user_name: uni.getStorageSync('user_name'),
									studentID: res.content
								},
								success: (res) => {
									console.log('--' + JSON.stringify(
										res));
									if (res.result.updated > 0) {
										uni.showToast({
											title: 'Edit successfully!'
										})
										that.getinfo()
									} else {
										uni.showToast({
											title: "No change",
											icon: 'error'
										})
									}
								}
							})
						}
					}
				})
			},
			getinfo() {
				this.list = [];
				uniCloud.callFunction({
					name: 'getinfo',
					data: {
						keyword: this.searchText,
						user_name: uni.getStorageSync('user_name')
					},
					success: (res) => {
						if (res.result.data) {
							res.result.data.forEach(dd => {
								this.list.push(dd)
							});
						}
						console.log('note:' + JSON.stringify(res));
					}
				})
			},
			Gender() {
				let that = this;
				uni.showActionSheet({
					itemList: ['Man', 'Woman'],
					success: function(res) {
						if (res.tapIndex == 0) {
							uniCloud.callFunction({
								name: 'editgender',
								data: {
									user_name: uni.getStorageSync('user_name'),
									gender: "Man"
								},
								success: (res) => {
									console.log('--' + JSON.stringify(
										res));
									if (res.result.updated > 0) {
										uni.showToast({
											title: 'edit successfully!'
										})
										that.getinfo();
									} else {
										uni.showToast({
											title: "No change"
										})
									}
								}
							})
						} else if (res.tapIndex == 1) {
							uniCloud.callFunction({
								name: 'editgender',
								data: {
									user_name: uni.getStorageSync('user_name'),
									gender: "Woman"
								},
								success: (res) => {
									console.log('--' + JSON.stringify(
										res));
									if (res.result.updated > 0) {
										uni.showToast({
											title: 'edit successfully!'
										})
										that.getinfo();
									} else {
										uni.showToast({
											title: "No change"
										})
									}
								}
							})
						}
					}
				})
			},
			Class() {
				let that = this;
				uni.showModal({
					title: 'edit Class',
					editable: true,
					success: function(res) {
						if (res.confirm) {
							console.log('edit your class')
							uniCloud.callFunction({
								name: 'editclass',
								data: {
									user_name: uni.getStorageSync('user_name'),
									class: res.content
								},
								success: (res) => {
									console.log('--' + JSON.stringify(
										res));
									if (res.result.updated > 0) {
										uni.showToast({
											title: 'Edit successfully!'
										})
										that.getinfo()
									} else {
										uni.showToast({
											title: "No change",
											icon: 'error'
										})
									}
								}
							})
						}
					}
				})
			},
			ChineseName() {
				let that = this;
				uni.showModal({
					title: 'edit chinese name',
					editable: true,
					success: function(res) {
						if (res.confirm) {
							console.log('edit your chinese name')
							uniCloud.callFunction({
								name: 'editchinesename',
								data: {
									user_name: uni.getStorageSync('user_name'),
									chinese_name: res.content
								},
								success: (res) => {
									console.log('--' + JSON.stringify(
										res));
									if (res.result.updated > 0) {
										uni.showToast({
											title: 'Edit successfully!'
										})
										that.getinfo()
									} else {
										uni.showToast({
											title: "No change",
											icon: 'error'
										})
									}
								}
							})
						}
					}
				})
			},
			EnglishName() {
				let that = this;
				uni.showModal({
					title: 'edit english name',
					editable: true,
					success: function(res) {
						if (res.confirm) {
							console.log('edit your english name')
							uniCloud.callFunction({
								name: 'editenglishname',
								data: {
									user_name: uni.getStorageSync('user_name'),
									english_name: res.content
								},
								success: (res) => {
									console.log('--' + JSON.stringify(
										res));
									if (res.result.updated > 0) {
										uni.showToast({
											title: 'Edit successfully!'
										})
										that.getinfo()
									} else {
										uni.showToast({
											title: "No change",
											icon: 'error'
										})
									}
								}
							})
						}
					}
				})
			},
			Subject() {
				let that = this;
				uni.showModal({
					title: 'edit your subject',
					editable: true,
					success: function(res) {
						if (res.confirm) {
							console.log('edit your subject')
							uniCloud.callFunction({
								name: 'editsubject',
								data: {
									user_name: uni.getStorageSync('user_name'),
									subject: res.content
								},
								success: (res) => {
									console.log('--' + JSON.stringify(
										res));
									if (res.result.updated > 0) {
										uni.showToast({
											title: 'Edit successfully!'
										})
										that.getinfo()
									} else {
										uni.showToast({
											title: "No change",
											icon: 'error'
										})
									}
								}
							})
						}
					}
				})
			},
			Email() {
				let that = this;
				uni.showModal({
					title: 'edit your email',
					editable: true,
					success: function(res) {
						if (res.confirm) {
							console.log('edit your email')
							uniCloud.callFunction({
								name: 'editemail',
								data: {
									user_name: uni.getStorageSync('user_name'),
									student_email: res.content
								},
								success: (res) => {
									console.log('--' + JSON.stringify(
										res));
									if (res.result.updated > 0) {
										uni.showToast({
											title: 'Edit successfully!'
										})
										that.getinfo()
									} else {
										uni.showToast({
											title: "No change",
											icon: 'error'
										})
									}
								}
							})
						}
					}
				})
			},
			Telephone() {
				let that = this;
				uni.showModal({
					title: 'edit your telephone',
					editable: true,
					success: function(res) {
						if (res.confirm) {
							console.log('edit your telephone')
							uniCloud.callFunction({
								name: 'edittelephone',
								data: {
									user_name: uni.getStorageSync('user_name'),
									telephone: res.content
								},
								success: (res) => {
									console.log('--' + JSON.stringify(
										res));
									if (res.result.updated > 0) {
										uni.showToast({
											title: 'Edit successfully!'
										})
										that.getinfo()
									} else {
										uni.showToast({
											title: "No change",
											icon: 'error'
										})
									}
								}
							})
						}
					}
				})
			},

		}
	}
</script>

<style lang="scss">
	.title {
		text-align: center;
		display: block;
		padding: 50rpx 35rpx 38rpx 35rpx;
		font-size: 32rpx;
		font-weight: bolder;
		color: black;
	}

	.text {
		font-size: 12px;
	}

	.menu-item {
		display: flex;
		align-items: center;
		padding: 5px;
		// 	border-bottom: 1rpx solid gray;

	}

	.menu {
		height: 100%;
		background-color: white;
	}
	.con{
		font-size: 28rpx;
		font-weight: bolder;
		color: black;
		margin-left: 10px;
	}
</style>