<template>
	<view>
		<text class="title">Schedule</text>
		<view class="date">Monday</view>
		<view class="center">
			<view v-for="(item,index) in list">
				<view class="kuai2" v-if="item.Monday" @longpress="opt(item._id)">
					{{item.subject}}
					{{item.teacher}}
					{{item.classroom}}
					{{item.time}}
				</view>
			</view>
		</view>
		<view class="date">Tuesday</view>
		<view class="center">
			<view v-for="(item,index) in list">
				<view class="kuai2" v-if="item.Tuesday">
					{{item.subject}}
					{{item.teacher}}
					{{item.classroom}}
					{{item.time}}
				</view>
			</view>
		</view>
		<view class="date">Wednesday</view>
		<view class="center">
			<view v-for="(item,index) in list">
				<view class="kuai2" v-if="item.Wednesday">
					{{item.subject}}
					{{item.teacher}}
					{{item.classroom}}
					{{item.time}}
				</view>
			</view>
		</view>
		<view class="date">Thursday</view>
		<view class="center">
			<view v-for="(item,index) in list">
				<view class="kuai2" v-if="item.Thursday">
					{{item.subject}}
					{{item.teacher}}
					{{item.classroom}}
					{{item.time}}
				</view>
			</view>
		</view>
		<view class="date">Friday</view>
		<view class="center">
			<view v-for="(item,index) in list">
				<view class="kuai2" v-if="item.Friday">
					{{item.subject}}
					{{item.teacher}}
					{{item.classroom}}
					{{item.time}}
				</view>
			</view>
		</view>
		<view class="tu">
			<image class="add" src="../../static/add.png" @tap="goto()"></image>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				list: []
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
			}
		},
		onShow() {
			this.getschedule()
		},
		methods: {
			goto() {
				uni.navigateTo({
					url: '/pages/addschedule/addschedule'
				})
			},
			getschedule() {
				this.list = [];
				uniCloud.callFunction({
					name: 'getschedule',
					data: {
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
			opt(_id) {
				let that = this;
				uni.showActionSheet({
					itemList: ['edit', 'delete'],
					success: function(res) {
						if (res.tapIndex == 0) {
							uni.navigateTo({
								url: '/pages/editschedule/editschedule?schedule_id=' + _id
							})
						} else if (res.tapIndex == 1) {
							uni.showModal({
								title: 'hint',
								content: 'Are you sure to delete this schedule?',
								success: function(res) {
									if (res.confirm) {
										console.log('delete')
										uniCloud.callFunction({
											name: 'deleteschedule',
											data: {
												schedule_id: _id
											},
											success: (res) => {
												console.log('--' + JSON.stringify(
													res));
												if (res.result.deleted > 0) {
													uni.showToast({
														title: 'Delete successfully!'
													})
													that.getschedule();
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
		}
	}
</script>

<style lang="scss">
	page{
		background-image: linear-gradient(208deg, #f3f3dc 10%, #cacaff 20%, #f8f6df 50%);
	}
	.bg-set {
		position: fixed;
		width: 100%;
		height: 100%;
		top: 0;
		left: 0;
		z-index: -1;
	}

	.title {
		text-align: center;
		display: block;
		padding: 50rpx 35rpx 38rpx 35rpx;
		font-size: 32rpx;
		font-weight: bolder;
		color: black;
	}

	.date {
		padding: 50rpx 35rpx 38rpx 35rpx;
		font-size: 32rpx;
		font-weight: bolder;
		color: black;
		position: relative;

		&::after {
			content: '';
			position: absolute;
			left: 13rpx;
			background-color: #2eeaf4;
			width: 12rpx;
			height: 33%;
			bottom: 37rpx;
			border-radius: 10rpx;
		}
	}

	.center {
		min-height: 250rpx;
		padding-top: 10rpx;
		border-radius: 38rpx;
		box-shadow: #ccc 8rpx 8rpx 8rpx;
		color: #191919;
		background-image: linear-gradient(0deg, #55ffff 10%, #f8f8f8 100%);
		display: flex;
		width: 100%;
		flex-direction: column;
	}

	image {
		position: fixed;
		bottom: 0;
		right: 0;
		height: 70px;
		width: 70px;
	}
	.kuai2 {
		background-color: white;
		border-radius: 25rpx;
		margin-top: 10rpx;
		margin-left: 15rpx;
		box-shadow: #ccc 8rpx 8rpx 8rpx;
		width: 75%;
	}
</style>