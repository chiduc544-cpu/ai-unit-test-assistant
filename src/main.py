#!/usr/bin/env python3
"""Main CLI Entry Point"""

import logging
import logging.config
from typing import Optional
from colorama import init, Fore, Back, Style
from config.settings import LOG_CONFIG
from src.ai_assistant import AITestAssistant

# Initialize colorama for cross-platform colored terminal text
init(autoreset=True)

# Setup logging
logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger(__name__)


class TestAssistantCLI:
    """Command-line interface for AI Test Assistant"""

    def __init__(self):
        """Initialize CLI"""
        self.assistant = AITestAssistant()
        self.running = True
        logger.info("CLI initialized")

    def print_header(self):
        """Print application header"""
        header = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗{Style.RESET_ALL}
{Fore.CYAN}║{Style.RESET_ALL}   {Fore.YELLOW}🤖 AI Unit Test Assistant{Style.RESET_ALL}                          {Fore.CYAN}║{Style.RESET_ALL}
{Fore.CYAN}║{Style.RESET_ALL}   Powered by OpenAI GPT-4 Turbo                    {Fore.CYAN}║{Style.RESET_ALL}
{Fore.CYAN}║{Style.RESET_ALL}   Type 'help' for available commands               {Fore.CYAN}║{Style.RESET_ALL}
{Fore.CYAN}╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
        """
        print(header)

    def print_success(self, message: str):
        """Print success message"""
        print(f"{Fore.GREEN}✓{Style.RESET_ALL} {message}")

    def print_error(self, message: str):
        """Print error message"""
        print(f"{Fore.RED}✗{Style.RESET_ALL} {message}")

    def print_info(self, message: str):
        """Print info message"""
        print(f"{Fore.BLUE}ℹ{Style.RESET_ALL} {message}")

    def handle_generate(self, args: str):
        """Handle generate command"""
        try:
            if not args:
                self.print_error("Please provide code to generate tests for")
                return
            
            self.print_info("Generating unit tests...")
            result = self.assistant.generate_tests(args)
            print(f"\n{Fore.CYAN}Generated Tests:{Style.RESET_ALL}")
            print(result)
            self.print_success("Tests generated successfully")
        except Exception as e:
            self.print_error(f"Error generating tests: {str(e)}")
            logger.error(f"Generate error: {str(e)}")

    def handle_analyze(self, args: str):
        """Handle analyze command"""
        try:
            if not args:
                self.print_error("Please provide test code to analyze")
                return
            
            self.print_info("Analyzing tests...")
            result = self.assistant.analyze_tests(args)
            print(f"\n{Fore.CYAN}Analysis Results:{Style.RESET_ALL}")
            print(result['analysis'])
            self.print_success("Analysis complete")
        except Exception as e:
            self.print_error(f"Error analyzing tests: {str(e)}")
            logger.error(f"Analyze error: {str(e)}")

    def handle_optimize(self, args: str):
        """Handle optimize command"""
        try:
            if not args:
                self.print_error("Please provide test code to optimize")
                return
            
            self.print_info("Optimizing tests...")
            suggestions = self.assistant.optimize_tests(args)
            print(f"\n{Fore.CYAN}Optimization Suggestions:{Style.RESET_ALL}")
            for i, suggestion in enumerate(suggestions, 1):
                print(f"  {i}. {suggestion}")
            self.print_success("Optimization suggestions provided")
        except Exception as e:
            self.print_error(f"Error optimizing tests: {str(e)}")
            logger.error(f"Optimize error: {str(e)}")

    def handle_debug(self, args: str):
        """Handle debug command"""
        try:
            if not args:
                self.print_error("Please provide test code and error message")
                return
            
            # Split by first occurrence of '|||' to separate test code and error
            parts = args.split('|||', 1)
            if len(parts) != 2:
                self.print_error("Format: debug <test_code> ||| <error_message>")
                return
            
            test_code, error_msg = parts
            self.print_info("Debugging test...")
            result = self.assistant.debug_test(test_code.strip(), error_msg.strip())
            print(f"\n{Fore.CYAN}Debug Report:{Style.RESET_ALL}")
            print(result)
            self.print_success("Debug analysis complete")
        except Exception as e:
            self.print_error(f"Error debugging test: {str(e)}")
            logger.error(f"Debug error: {str(e)}")

    def handle_refactor(self, args: str):
        """Handle refactor command"""
        try:
            if not args:
                self.print_error("Please provide test code to refactor")
                return
            
            self.print_info("Refactoring tests...")
            result = self.assistant.refactor_tests(args)
            print(f"\n{Fore.CYAN}Refactored Code:{Style.RESET_ALL}")
            print(result)
            self.print_success("Tests refactored successfully")
        except Exception as e:
            self.print_error(f"Error refactoring tests: {str(e)}")
            logger.error(f"Refactor error: {str(e)}")

    def handle_coverage(self, args: str):
        """Handle coverage command"""
        try:
            if not args:
                self.print_error("Please provide source code and test code")
                return
            
            parts = args.split('|||', 1)
            if len(parts) != 2:
                self.print_error("Format: coverage <source_code> ||| <test_code>")
                return
            
            source_code, test_code = parts
            self.print_info("Estimating coverage...")
            result = self.assistant.estimate_coverage(source_code.strip(), test_code.strip())
            print(f"\n{Fore.CYAN}Coverage Estimate:{Style.RESET_ALL}")
            print(result['coverage_estimate'])
            self.print_success("Coverage estimation complete")
        except Exception as e:
            self.print_error(f"Error estimating coverage: {str(e)}")
            logger.error(f"Coverage error: {str(e)}")

    def handle_chat(self, args: str):
        """Handle chat command"""
        try:
            if not args:
                self.print_error("Please provide a message")
                return
            
            self.print_info("Processing...")
            response = self.assistant.chat(args)
            print(f"\n{Fore.CYAN}Assistant:{Style.RESET_ALL}")
            print(response)
        except Exception as e:
            self.print_error(f"Error: {str(e)}")
            logger.error(f"Chat error: {str(e)}")

    def handle_command(self, command: str):
        """Parse and handle user command"""
        parts = command.split(None, 1)
        if not parts:
            return
        
        cmd = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        
        commands = {
            'generate': self.handle_generate,
            'analyze': self.handle_analyze,
            'optimize': self.handle_optimize,
            'debug': self.handle_debug,
            'refactor': self.handle_refactor,
            'coverage': self.handle_coverage,
            'chat': self.handle_chat,
            'help': lambda x: print(self.assistant.get_help()),
            'clear': lambda x: self.assistant.clear_history() or self.print_success("History cleared"),
            'exit': lambda x: self.quit(),
        }
        
        if cmd in commands:
            commands[cmd](args)
        else:
            self.print_error(f"Unknown command: {cmd}. Type 'help' for available commands.")

    def quit(self):
        """Quit the application"""
        print(f"\n{Fore.YELLOW}Thank you for using AI Unit Test Assistant!{Style.RESET_ALL}")
        self.running = False

    def run(self):
        """Run the CLI application"""
        self.print_header()
        print(f"{Fore.YELLOW}Type 'help' for available commands or 'exit' to quit.{Style.RESET_ALL}\n")
        
        while self.running:
            try:
                user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()
                if user_input:
                    self.handle_command(user_input)
            except KeyboardInterrupt:
                print(f"\n{Fore.YELLOW}Interrupted by user{Style.RESET_ALL}")
                self.quit()
            except Exception as e:
                self.print_error(f"An error occurred: {str(e)}")
                logger.error(f"CLI error: {str(e)}")


def main():
    """Main entry point"""
    cli = TestAssistantCLI()
    cli.run()


if __name__ == '__main__':
    main()
