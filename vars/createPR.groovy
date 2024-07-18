
def call(String repoUrl, String sourceBranch, String destinationBranch, String prTitle, String prBody, String credentialsId ) {
    def scriptPath = libraryResource('scripts/create_pr.py')
    writeFile file: 'create_pr.py', text: scriptPath

    withCredentials([usernamePassword(credentialsId: credentialsId, passwordVariable: 'GITHUB_TOKEN', usernameVariable: 'GITHUB_USERNAME')]) {
        sh '''
            pip3 install requests
            python3 create_pr.py ${repoUrl} ${sourceBranch} ${destinationBranch} "${prTitle}" "${prBody}" $GITHUB_TOKEN
        '''
    }
}