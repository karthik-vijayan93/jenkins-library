
def call(String repoUrl, String sourceBranch, String destinationBranch, String prTitle) {
    def scriptPath = libraryResource('scripts/create_pr.py')
    writeFile file: 'create_pr.py', text: scriptPath

    sh """
        pip3 install requests
        python3 create_pr.py ${repoUrl} ${sourceBranch} ${destinationBranch} "${prTitle}"
    """
}
