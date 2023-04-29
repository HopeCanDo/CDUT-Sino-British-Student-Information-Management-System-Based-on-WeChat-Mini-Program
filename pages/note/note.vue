<template>
	<view class="container">
		<view class="title"><text>All Note</text></view>
		<view class="fu"><text>{{notecount}} notes</text></view>
		<view>
			<view><input v-model="searchText" confirm-type="search" @confirm="getnote()" placeholder="search note" />
			</view>
		</view>
		<view v-for="(item,index) in list" @longpress="opt(item._id)" class="cont">
			<view class="tt">{{item.content}}</view>
			<view class="fu1">{{item.createdtime}}</view>
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
				notecount: 0
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
				this.getnoteCount();
			}
		},
		onShow() {
			this.getnoteCount();
			this.getnote();
		},
		methods: {
			goto() {
				uni.redirectTo({
					url: '../addnote/addnote'
				})
			},
			getnote() {
				this.list = [];
				uniCloud.callFunction({
					name: 'getnote',
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
								url: '/pages/editnote/editnote?note_id=' + _id
							})
						} else if (res.tapIndex == 1) {
							uni.showModal({
								title: 'hint',
								content: 'Are you sure to delete this note?',
								success: function(res) {
									if (res.confirm) {
										console.log('delete')
										uniCloud.callFunction({
											name: 'deletenode',
											data: {
												note_id: _id
											},
											success: (res) => {
												console.log('--' + JSON.stringify(
													res));
												if (res.result.deleted > 0) {
													uni.showToast({
														title: 'Delete successfully!'
													})
													that.getnoteCount();
													that.getnote();
												} else {
													uni.showToast({
														title: "Delete Failed",
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
			getnoteCount() {
				uniCloud.callFunction({
					name: 'notecount',
					data: {user_name:uni.getStorageSync('user_name')},
					success: (res) => {
						console.log('----' + JSON.stringify(res))
						this.notecount = res.result.total;
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