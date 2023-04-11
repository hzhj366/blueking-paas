/*
 * TencentBlueKing is pleased to support the open source community by making
 * 蓝鲸智云 - PaaS 平台 (BlueKing - PaaS System) available.
 * Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
 * Licensed under the MIT License (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 *	http://opensource.org/licenses/MIT
 *
 * Unless required by applicable law or agreed to in writing, software distributed under
 * the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
 * either express or implied. See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * We undertake not to change the open source license (MIT license) applicable
 * to the current version of the project delivered to anyone in the future.
 */

package app

import (
	"fmt"

	"github.com/spf13/cobra"
)

// NewCmdDeploy returns a Command instance for 'app deploy' sub command
func NewCmdDeploy() *cobra.Command {
	cmd := cobra.Command{
		Use:   "deploy",
		Short: "Deploy PaaS application",
		Run: func(cmd *cobra.Command, args []string) {
			deployApp()
		},
	}

	cmd.Flags().StringVarP(&appCode, "code", "", "", "app code")
	cmd.Flags().StringVarP(&appModule, "module", "", "default", "module name")
	cmd.Flags().StringVarP(&appEnv, "env", "", "prod", "environment (stag/prod)")
	_ = cmd.MarkFlagRequired("code")

	return &cmd
}

// 应用部署
func deployApp() {
	// TODO 执行应用部署操作
	fmt.Println("Implement me...")
}