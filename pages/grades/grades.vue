<template>
	<view class="container">
		<view class="title"><text>All Grades</text></view>
		<view class="fu"><text>{{gradecount}} grades</text></view>
		<view>
			<view><input v-model="searchText" confirm-type="search" @confirm="getgrades()" placeholder="search subject" />
			</view>
		</view>
		<view v-for="(item,index) in list" @longpress="opt(item._id)" class="cont">
			<view class="tt">{{item.content}}</view>
			<view class="fu1">Level:{{item.level}} Score:{{item.score}}</view>
		</view>
		<view class="tu">
			<image class="add" src="../../static/add.png" @tap="goto"></image>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				list: [],
				searchText: '',
				gradecount: 0
			}
		},
		onLoad() {
			if (!uni.getStorageSync('user_name')) {
				uni.showToast({
					title: 'Please login!',
					icon: 'error'
				})
				uni.navigateTo({
					url: '/pages/login/login'
				})
			}else{
				this.getgradeCount();
			}
		},
		onShow() {
			this.getgradeCount();
			this.getgrade();
		},
		methods: {
			goto() {
				uni.redirectTo({
					url: '../addgrade/addgrade'
				})
			},
			getgrade() {
				this.list = [];
				uniCloud.callFunction({
					name: 'getgrade',
					data: {
						keyword: this.searchText,
						user_name:uni.getStorageSync('user_name')
					},
					success: (res) => {
						if (res.result.data) {
							res.result.data.forEach(dd => {
								this.list.push(dd)
							});
						}
						console.log('grades:' + JSON.stringify(res));
					}
				})
			},
			opt(_id) {
				let that = this;
				uni.showActionSheet({
					itemList: ['edit', 'delete'],
					success: function(res) {
						if (res.tapIndex == 0) {
							uni.navigateTo({
								url: '/pages/editgrade/editgrade?grade_id=' + _id
							})
						} else if (res.tapIndex == 1) {
							uni.showModal({
								title: 'hint',
								content: 'Are you sure to delete this grade?',
								success: function(res) {
									if (res.confirm) {
										console.log('delete')
										uniCloud.callFunction({
											name: 'deletegrade',
											data: {
												grade_id: _id
											},
											success: (res) => {
												console.log('--' + JSON.stringify(
													res));
												if (res.result.deleted > 0) {
													uni.showToast({
														title: 'Delete successfully!'
													})
													that.getgradeCount();
													that.getgrade();
												} else {
													uni.showToast({
														title: "Delete failed",
														icon: 'error'
													})
												}
											}
										})
									}
								}
							})
						}
					}
				})
			},
			getgradeCount() {
				uniCloud.callFunction({
					name: 'gradecount',
					data: {user_name:uni.getStorageSync('user_name')},
					success: (res) => {
						console.log('----' + JSON.stringify(res))
						this.gradecount = res.result.total;
					}
				})
			}

		}
	}
</script>

<style>
	page {
		padding: 1%;
		background-image: linear-gradient(208deg, #f3f3dc 10%, #cacaff 20%, #f8f6df 50%);
	}

	.title {
		font-size: 50rpx;
	}

	.fu {
		color: #8f8f94;
	}

	.fu1 {
		color: #8f8f94;
		margin-left: 20rpx;
		margin-top: 15rpx;
	}

	input {
		height: 70rpx;
		background-color: #dddddd;
		background-image: url(../../static/search.png);
		background-repeat: no-repeat;
		background-size: 50rpx;
		margin-top: 20rpx;
		border-radius: 50rpx;
		background-position: 30rpx 15rpx;
		padding-left: 90rpx;
		width: 500rpx;
	}

	image {
		position: fixed;
		bottom: 0;
		right: 0;
		height: 70px;
		width: 70px;
	}

	.cont {
		border-bottom: 1rpx solid gray;
	}
</style>